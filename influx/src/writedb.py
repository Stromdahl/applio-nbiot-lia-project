from typing import Any

from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS


def write_points(client, bucket, org, sequence):
    write_api = client.write_api(write_options=SYNCHRONOUS)
    for point in sequence:
        write_api.write(bucket, org, point)

def _prepare_point(measurement, data) -> Point:
    return Point(measurement)\
        .tag("application_name", data['application_name'])\
        .tag("dev_eui", data['device_id'])\
        .tag("device_name", data['device_id'])\
        .tag("f_port", 1)\
        .tag("host", "nb-iot-stack")\

def prepare_data(data):
    """Handles the perperation of the data for inserting to influxdb"""
    device_id = data['device_id']
    application_name = data['application_name']

    result = []
    for measurement, value in data["measurement"].items():
        point = _prepare_point("device_frmpayload_data_"+ measurement, data)
        point = point.field("value", value)
        result.append(point)

    for measurement, value in data["device_uplink"].items():
        point = _prepare_point("device_uplink", data)
        point = point.field(measurement, value)
        result.append(point)
    return result 


# # https://docs.influxdata.com/telegraf/v1.22/data_formats/input/json_v2/
# def write_json():
#     json_payload = []

#     measurement = "counter_a"
#     value = 123
#     device_id = "c1d3b6f9"
#     application_name = "abc123"

#     Point("mem")\
#         .tag("host", "host1")\
#         .field("value", value)

#     data = {
#         "measurement": f"device_frmpayload_data_{measurement}",
#         "tags": {
#             "application_name": application_name,
#             "dev_eui": device_id,
#             "device_name": device_id,
#             "f_port": 1,
#             "host": "nb-iot-stack"
#         },
#         "fields": {
#             "value": value
#         }
#     }

#     json_payload.append(data)
#     print(json_payload)
#     write_api.write(bucket=bucket, org=org, record=json_payload)
