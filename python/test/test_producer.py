import json
from .. import AvroProducer, settings

data = {
    "acheckbox": False,
    "anumber": 123,
}

data_v2 = {
    "checkbox_v2": False,
    "number_v2": 123,
}

try:
    p = AvroProducer.AvroProducer({"bootstrap.servers": "localhost:9092"})
    for val in range(1, 5):
        data["aname"] = f"name-{val}"
        p.produce(settings.TOPIC_NAME, data, "1")
        p.poll(0.5)

    for val in range(1, 5):
        data_v2["name_v2"] = f"name-{val}"
        p.produce(settings.TOPIC_NAME, data_v2)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)