from __future__ import absolute_import

import apache_beam as beam
import argparse
import json
import logging
import os
from apache_beam.io.gcp.bigtableio import WriteToBigTable
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from google.cloud.bigtable import row as cbt_row
from google.protobuf import json_format

# from pipeline import afd_simplified_pb2, test_pb2
from beam_protos import afd_simplified_pb2

class TransformDictToBigTableRow(beam.DoFn):

    def process(self, row, **kwargs):
        row_key = row['identifier']

        direct_row = cbt_row.DirectRow(row_key=row_key)
        direct_row.set_cell('fares', "col1", json.dumps(row))
        yield direct_row


class TransformDictToProto(beam.DoFn):

    def process(self, row, **kwargs):
        result = json_format.ParseDict(row, afd_simplified_pb2.AFD())
        yield result


# class TransformProtoToBigTableRow(beam.DoFn):
#
#     def process(self, row, **kwargs):
#         row_key = row.event_metadata.unique_identifier
#         direct_row = cbt_row.DirectRow(row_key=row_key)
#         direct_row.set_cell('fares', "col2", row.SerializeToString())
#         yield direct_row

beam.coders.registry.register_coder(afd_simplified_pb2.AFD, beam.coders.ProtoCoder)

def run(argv=None):
    """Run the workflow."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_format', default="PROTO", choices=["JSON", "PROTO"])

    known_args, pipeline_args = parser.parse_known_args(argv)
    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = True

    fn = os.path.join(os.path.dirname(__file__), 'farestore_select_couchbase_fares.sql')

    with open(fn, 'r') as f:
        query_fares = f.read()

    with beam.Pipeline(options=pipeline_options) as p:

        query_fares = """
        SELECT distinct loc as identifier FROM `lookerdata.cdc.project_tycho_reports` LIMIT 1000
        """

        # Reading fare data from BigQuery
        pcoll_fares = p | 'Read Fares' >> beam.io.Read(beam.io.BigQuerySource(query=query_fares, use_standard_sql=True))

        # generate row key....

        # # Converting dict to proto to BigTable row
        # if known_args.output_format == "PROTO":
        #     cbt_fares = (pcoll_fares
        #                  | 'Convert to proto' >> beam.ParDo(TransformDictToProto())
        #                  | 'Create BigTable Rows' >> beam.ParDo(TransformProtoToBigTableRow())
        #                  )
        # # Converting dict to json to BigTable row
        # else:
        #     cbt_fares = pcoll_fares | 'Create BigTable Rows' >> beam.ParDo(TransformDictToBigTableRow())

        f = pcoll_fares | 'Convert to proto' >> beam.ParDo(TransformDictToProto())

        res = f | beam.io.WriteToText('pipeline/output.txt')
        # # Converting dict to proto to BigTable row
        # if known_args.output_format == "PROTO":
        #     cbt_fares = (pcoll_fares
        #                  | 'Convert to proto' >> beam.Map(dict_to_proto)
        #                  | 'Create BigTable Rows' >> beam.Map(proto_to_cbt_row)
        #                  )
        # # Converting dict to json to BigTable row
        # else:
        #     cbt_fares = pcoll_fares | 'Create BigTable Rows' >> beam.Map(dict_to_cbt_row)

        # # pylint:disable=expression-not-assigned
        # cbt_fares | WriteToBigTable(project_id='travix-bi-test', instance_id='inst-fare-store',
        #                             table_id='unpriced-fares')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
