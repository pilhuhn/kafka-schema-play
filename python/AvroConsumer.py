from . import settings
from .registry import util

import avro.schema
import avro.io
from confluent_kafka import Consumer, KafkaError
import io

class AvroConsumer(Consumer):

    def __init__(self, consumer_settings):
        schema_json = util.retrive_schema(settings.AVRO_SCHEMA_NAME)
        schema = avro.schema.parse(schema_json)

        self.reader = avro.io.DatumReader(schema)
        super().__init__(consumer_settings)

    def poll(self, timeout):
        msg = super().poll(timeout)
        if msg is not None and not msg.error():
            bytes_reader = io.BytesIO(msg.value())
            decoder = avro.io.BinaryDecoder(bytes_reader)
            msg.set_value(self.reader.read(decoder))

        return msg

