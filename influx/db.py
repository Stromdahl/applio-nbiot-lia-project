import json
import os

from flask.cli import load_dotenv
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from influx.querydb import querydb
from influx.writedb import write_lines, write_point, write_json

load_dotenv()

token = os.getenv('token')
org = os.getenv('org')
bucket = os.getenv('bucket')
url = os.getenv('url')


client = InfluxDBClient(url=url, token=token, org=org, verify_ssl=None)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()


#write_lines()
write_point()
#write_json()

querydb()

client.close()
