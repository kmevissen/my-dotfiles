#!/usr/bin/env bash

python -m main \
--setup_file ./setup.py \
--job_name multi-file-proto-koen \
--project travix-bi-test \
--runner DataflowRunner \
--region europe-west1 \
--machine_type n1-standard-2 \
--staging_location gs://temp-travix-bi-test/farestore_save_to_bigtable/staging \
--temp_location gs://temp-travix-bi-test/farestore_save_to_bigtable/temp


