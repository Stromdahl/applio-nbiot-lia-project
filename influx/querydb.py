import json
import os

from flask.cli import load_dotenv
from influxdb_client import InfluxDBClient, Point

load_dotenv()

token = os.getenv('token')
org = os.getenv('org')
bucket = os.getenv('bucket')
url = os.getenv('url')

client = InfluxDBClient(url=url, token=token, org=org, verify_ssl=None)
query_api = client.query_api()


def querydb():
    query = """from(bucket: "testraw") |> range(start: -1000h)"""
    tables = client.query_api().query(query, org=org)
    for table in tables:
        for record in table.records:
            print(record)



'''
query = """from(bucket: "testraw") |> range(start: -100h)"""
tables = client.query_api().query(query, org=org)
for table in tables:
    for record in table.records:
        print(record)
'''