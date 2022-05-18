from email.mime import application
import json
import os
from influxdb_client import InfluxDBClient
import paho.mqtt.client as mqtt

from writedb import create_data_sequence, write_points

influx_token = os.getenv('INFLUX_TOKEN')
influx_org = os.getenv('INFLUX_ORG')
influx_url = os.getenv('INFLUX_URL')


def on_message(client: mqtt.Client, userData, message: mqtt.MQTTMessage):
    data = json.loads(message.payload.decode('utf-8'))
    application_name = data["application_name"]
    if application_name:
        result = create_data_sequence(data)
        bucket = "test"
        print(f'{data}')
        influx_client = InfluxDBClient(url=influx_url, token=influx_token)
        write_points(client=influx_client, bucket=bucket, org=influx_org, sequence=result)


def main():
    client = mqtt.Client()
    client.connect("mosquitto", 1883, 60)
    client.subscribe("gateway/#")

    client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    main()

    # device_frmpayload_data_battery
    # device_frmpayload_data_bytes
    # device_frmpayload_data_counter_a
    # device_frmpayload_data_counter_b
    # device_frmpayload_data_payload_counter
    # device_frmpayload_data_sensor_status
    # device_frmpayload_data_total_counter_a
    # device_frmpayload_data_total_counter_b

    # data = {
    #     "application_name": "abc123",
    #     "device_id": 'E8EB1BFF4F23',
    #     "device_uplink": {
    #         "rssi": 143
    #     },
    #     "measurement":{
    #         'device_status': 0,
    #         'battery_voltage': 2.41,
    #         'counter_a': 0,
    #         'counter_b': 0,
    #         'sensor_status': 162
    #     }
    # }