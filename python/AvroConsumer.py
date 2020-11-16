from . import settings
from .registry import util

import avro.io
from confluent_kafka import Consumer
import io


SCHEMA_WITH_HEADER = util.get_parsed_schema(settings.MESSAGE_SCHEMA_WITH_HEADER)

class AvroConsumer(Consumer):

    def poll(self, timeout):
        msg = super().poll(timeout)
        if msg is not None and not msg.error():
            data_with_header = self.deserialize_data(msg.value(), SCHEMA_WITH_HEADER)

            schema = util.retrieve_schema(settings.AVRO_SCHEMA_NAME, data_with_header.get("header").get("version"))
            value = self.deserialize_data(data_with_header.get("data"), schema)

            msg.set_value(value)
        return msg

    def deserialize_data(self, data, schema):
        reader = avro.io.DatumReader(schema)
        bytes_reader = io.BytesIO(data)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        return reader.read(decoder)
