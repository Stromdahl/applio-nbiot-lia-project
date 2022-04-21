import json
import os
from flask.cli import load_dotenv
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influx.querydb import querydb

load_dotenv()
token = os.getenv('token')
org = os.getenv('org')
bucket = os.getenv('bucket')
url = os.getenv('url')

client = InfluxDBClient(url=url, token=token, org=org, verify_ssl=None)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()


def write_point():
    p = Point("test_measurement").tag("location", "Lund").field("temperature", 22.1)
    # pcc = Point("xxx").tag("yy", "zz").field("ppp",123,3)
    write_api.write(bucket=bucket, record=p)


def write_lines():
    data = "mem,host=hostTest used_percent=20.1111111"
    write_api.write(bucket, org, data)


def write_json():
    data = {
        "measurement": "John",
        "age": 30,
        "city": "New York",
    }
    y = json.dumps(data)
    print(y)
    write_api.write(bucket=bucket, record=y)
