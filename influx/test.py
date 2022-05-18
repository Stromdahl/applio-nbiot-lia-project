from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "VU6i3UKfqeCkw-f3fSKZU2svjk34wyb6gHoABMhemdhpO4IjCrwlVDvA9L5CyN3xUdGjJMyQs2jqBfOMdbl2HQ=="
org = "myOrg"
bucket = "test2"

client = InfluxDBClient(url="http://localhost:8086", token=token)

print(client.health())


write_api = client.write_api(write_options=SYNCHRONOUS)

data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)
