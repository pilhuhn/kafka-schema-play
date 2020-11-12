from . import settings
from .registry import util

import avro.schema
import avro.io
from confluent_kafka import Producer
import io
import pdb


class AvroProducer(Producer):

    def __init__(self, server_config):
        schema_json = util.retrieve_schema(settings.AVRO_SCHEMA_NAME)

        schema = avro.schema.parse(schema_json)
        self.writer = avro.io.DatumWriter(schema)
        super().__init__(server_config)



    def produce(self, topic, data):
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        self.writer.write(data, encoder)
        raw_bytes = bytes_writer.getvalue()

        super().produce(topic, raw_bytes, callback=self.acked)

    def acked(self, err, msg):
        if err is not None:
            print("Failed to deliver message: {0}: {1}"
                .format(msg.value(), err.str()))
        else:
            print("Message produced: {0}".format(msg.value()))
