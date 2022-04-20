import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


influx_cloud_url = "url"
influx_cloud_token = os.getenv(
    "token")
influx_cloud_token = 'token'
bucket = "bucket"
org = "org"


client = InfluxDBClient(url=influx_cloud_url, token=influx_cloud_token, org=org, verify_ssl=None)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)


## using Table structure
tables = query_api.query('from(bucket:"testraw") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)



