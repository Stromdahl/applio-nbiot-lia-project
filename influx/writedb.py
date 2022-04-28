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
        "measurement": "device_frmpayload_data_analogInput_4",
        "tags": {
            "application_name": "server02",
            "device_name": "applio123",
            "dev_eui": 13413413431413,
            "host": "applio-stack-telegraf",
            "f-port": 99
        },
        "fields": {
            "value": 0.00000,
        }
    }

    dataTest = [
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": 3.051,
            "type": "BatV",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": "Interrupt Sensor send",
            "type": "Ext_sensor",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": "Low",
            "type": "Exti_pin_level",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": "False",
            "type": "Exti_status",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": "Sensor no connection",
            "type": "No_connect",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": 33.2,
            "type": "humidity",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        },
        {
            "sensor_id": "",
            "dev_eui": "a84041868182d48b",
            "data": 22.12,
            "type": "temperature",
            "receive_date": "2022-04-28T11:41:57.803422048Z"
        }
    ]

    json_payload.append(data)
    print(json_payload)
    write_api.write(bucket=bucket, org=org, record=json_payload)
