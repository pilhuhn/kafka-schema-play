AVRO_SCHEMA_NAME = "test-topic"
TOPIC_NAME = "test-topic"

MESSAGE_SCHEMA_WITH_HEADER = {
        "type": "record",
        "name": "schema_with_header",
        "fields": [
            {
                "name": "header",
                "type": {
                    "name": "header",
                    "type": "record",
                    "fields": [
                        {
                            "name": "version",
                            "type": "string"
                        }
                    ]
                }              
            },
            {
                "name": "data",
                "type": "bytes"
            }
        ]
    }
