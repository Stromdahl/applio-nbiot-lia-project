import json
import os
from datetime import datetime

from flask.cli import load_dotenv
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.write.point import Point, DEFAULT_WRITE_PRECISION

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
    p = Point("my_mem").tag("location", "Bara").field("temperature", 12.12)
    # pcc = Point("xxx").tag("yy", "zz").field("ppp",123,3)
    write_api.write(bucket, org, p)


def write_lines():
    data = "mem,host=hostTest used_percent=20.1111111"
    write_api.write(bucket, org, data)


# https://docs.influxdata.com/telegraf/v1.22/data_formats/input/json_v2/
def write_json():
    json_payload = []

    data = {
        "measurement": "whatever",
        "tags": {
            "location": "server01",
            "host": "applio"
        },
        "fields": {
            "filled_capacity": 0.123,
        }
    }
    json_payload.append(data)
    print(json_payload)
    write_api.write(bucket=bucket, org=org, record=json_payload)


    # data = ({"measurement": "h2o_feet", "tags": {"location": "coyote_creek"},
    # "fields": {"water_level": 1.0}, "time": 1})

    # y = json.dumps(data)
    # print(data)
    # print(data1)
    # client.write_api()
    # write_api.write(bucket, org, data1)
