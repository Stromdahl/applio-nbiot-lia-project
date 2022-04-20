import os

from flask.cli import load_dotenv
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()

token = os.getenv('token')
org = os.getenv('org')
bucket = os.getenv('bucket')
url = os.getenv('url')


client = InfluxDBClient(url=url, token=token, org=org, verify_ssl=None)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

''''
p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
#pcc = Point("xxx").tag("yy", "zz").field("ppp",123,3)
write_api.write(bucket=bucket, record=p)



write_api = client.write_api(write_options=SYNCHRONOUS)
data = "mem,host=host1 used_percent=23.43234543"
write_api.write(bucket, org, data)
'''

query = """from(bucket: "testraw") |> range(start: -100h)"""
tables = client.query_api().query(query, org=org)
for table in tables:
    for record in table.records:
        print(record)


client.close()
