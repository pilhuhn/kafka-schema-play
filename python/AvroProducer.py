from . import settings
from .registry import util

import avro.io
from confluent_kafka import Producer
import io

SCHEMA_WITH_HEADER = util.get_parsed_schema(settings.MESSAGE_SCHEMA_WITH_HEADER)

class AvroProducer(Producer):

    def produce(self, topic, data, schema_version=None):
        schema = util.retrieve_schema(settings.AVRO_SCHEMA_NAME, schema_version)

        raw_bytes = self.serialize_data(data, schema)

        data_with_header = {
            "header": {"version": str(schema_version)},
            "data": raw_bytes
        }

        message = self.serialize_data(data_with_header, SCHEMA_WITH_HEADER)

        super().produce(topic, message, callback=self.acked)

    def acked(self, err, msg):
        if err is not None:
            print("Failed to deliver message: {0}: {1}"
                .format(msg.value(), err.str()))
        else:
            print("Message produced: {0}".format(msg.value()))

    def serialize_data(self, data, schema):
        writer = avro.io.DatumWriter(schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(data, encoder)
        
        return bytes_writer.getvalue()


