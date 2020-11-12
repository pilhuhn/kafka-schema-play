from registry import util
import settings

# Upload the first version.
util.upload_schema(settings.AVRO_SCHEMA_NAME, "avro/test1.avsc")

# Upload the updated version.
util.upload_schema(settings.AVRO_SCHEMA_NAME, "avro/test1-v2.avsc")