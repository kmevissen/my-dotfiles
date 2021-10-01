from __future__ import absolute_import

import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions
from google.protobuf import json_format

from pipeline import test_pb2


class TransformDictToProto(beam.DoFn):

    def process(self, row, **kwargs):
        d = dict({'identifier': row})
        result = json_format.ParseDict(d, test_pb2.Example())
        yield result


class ConvertProtoToJson(beam.DoFn):

    def process(self, row, **kwargs):
        yield json_format.MessageToJson(row)


def run(argv=None):
    """Run the workflow."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default="pipeline/input.txt")
    parser.add_argument('--output', default="pipeline/output.txt")

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    # pipeline_options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=pipeline_options) as p:
        lines = p | 'Read' >> beam.io.ReadFromText(known_args.input)

        pr = lines | 'Convert to Proto' >> beam.ParDo(TransformDictToProto())

        bts = pr | 'Convert to Bytes' >> beam.ParDo(ConvertProtoToJson())

        bts | beam.io.WriteToText(known_args.output)
