package com.travix.experiments;

import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.PipelineResult;
import org.apache.beam.sdk.coders.BigEndianIntegerCoder;
import org.apache.beam.sdk.coders.KvCoder;
import org.apache.beam.sdk.coders.StringUtf8Coder;
import org.apache.beam.sdk.io.FileIO;
import org.apache.beam.sdk.io.jdbc.JdbcIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

import java.io.Console;
import java.sql.ResultSet;

public class RdmbsExtractPipeline {
    public static void main(String[] args) {
        Logger log = LogManager.getLogger(RdmbsExtractPipeline.class);

        // Start by defining the options for the pipeline.
        PipelineOptions options = PipelineOptionsFactory.create();

        Pipeline pipeline = Pipeline.create(options);

//        PCollection<KV<Integer, String>> r = pipeline.apply(JdbcIO.<KV<Integer, String>>read()
//                        .withDataSourceConfiguration(JdbcIO.DataSourceConfiguration.create(
//                                "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jdbc:sqlserver://35.187.79.51:1433;databaseName=REP_UNIT4_PRD;user=ETLFramework;password=ETLFramework")
//                        )
//                        .withQuery("select distinct agrtid, client_name from acrclient")
//                        .withCoder(KvCoder.of(BigEndianIntegerCoder.of(), StringUtf8Coder.of()))
//                        .withRowMapper(new JdbcIO.RowMapper<KV<Integer, String>>() {
//                            public KV<Integer, String> mapRow(ResultSet resultSet) throws Exception {
//                                return KV.of(resultSet.getInt(1), resultSet.getString(2));
//                            }
//                        })
//        ).apply(
//                "LogToConsole",                     // the transform name
//                ParDo.of(new DoFn<KV<Integer, String>, KV<Integer, String>>() {    // a DoFn as an anonymous inner class instance
//                    @ProcessElement
//                    public void processElement(@Element KV<Integer, String> e, OutputReceiver<KV<Integer, String>> out) {
//
//
//                        System.out.println(String.format("key: %d | value: %s", e.getKey(), e.getValue()));
//                        out.output(e);
//                    }
//                }));

        PCollection<Object> r = pipeline.apply(JdbcIO.read()
                .withDataSourceConfiguration(JdbcIO.DataSourceConfiguration.create(
                        "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jdbc:sqlserver://35.187.79.51:1433;databaseName=REP_UNIT4_PRD;user=ETLFramework;password=ETLFramework")
                )
                .withQuery("select distinct agrtid, client_name from acrclient")
//                .withCoder(KvCoder.of(BigEndianIntegerCoder.of(), StringUtf8Coder.of()))
                .withRowMapper(new JdbcIO.RowMapper<Object>() {
                    public Object mapRow(ResultSet resultSet) throws Exception {
                        ResultSet
                        return Object;
                    })
        );

        PipelineResult.State result = pipeline.run().waitUntilFinish();
        System.out.println("Done");

    }
}
