import json
from .. import AvroProducer, settings

data = {
    "aname": "test_name",
    "acheckbox": False,
    "anumber": 1237859,
}

try:
    p = AvroProducer.AvroProducer({"bootstrap.servers": "localhost:9092"})
    for val in range(1, 5):
        data["aname"] = f"name-{val}"
        p.produce(settings.TOPIC_NAME, data)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)