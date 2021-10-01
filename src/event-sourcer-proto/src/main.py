#!/usr/bin/env python

import logging

from proto import message_pb2
from proto.shared import metadata_pb2
import threading
from google.protobuf.json_format import MessageToDict
from datetime import datetime
import json
import os
from google.cloud import pubsub
from google.cloud.exceptions import NotFound
import uuid

LOG_FORMAT = '%(message)s'
LOG_LEVEL = 'INFO'
LOGGER = logging.getLogger(__name__)

MESSAGE_PER_SEC = int(os.getenv('MESSAGE_PER_SEC', 50))


client = pubsub.PublisherClient()
topic = client.topic_path('travix-bi-test', 'protobuf_test_koen')
# client.create_topic(topic)
try:
    response = client.get_topic(topic)
except NotFound:
    response = client.create_topic(topic)


def publish(log_message):
    # LOGGER.info(json.dumps(MessageToDict(log_message)))

    data = log_message.SerializeToString()
    response = client.publish(topic, data, username='koen', type='proto')
    LOGGER.info(response.result())


def log_events():
    threading.Timer(1, log_events).start()

    for i in range(MESSAGE_PER_SEC):
        metadata = metadata_pb2.MetaData()
        metadata.unique_id = str(uuid.uuid4())
        metadata.session_id = str(uuid.uuid4())
        metadata.request_id = str(uuid.uuid4())
        metadata.message_type = "protocol_buffer_test"

        publish(metadata)


def main():
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    log_events()


if __name__ == '__main__':
    main()