import os
from influxdb_client import InfluxDBClient, Point
import paho.mqtt.client as mqtt


from writedb import prepare_data, write_points

token = os.getenv('token')
org = os.getenv('org')
url = os.getenv('influx_url')

client = InfluxDBClient(url=url, token=token)

health = client.health()

def main():
    print(url)
    if(health.status == "fail"):
        print("No connection to influx, health status 'Fail'")
        return 0
    
    
    # device_frmpayload_data_battery
    # device_frmpayload_data_bytes
    # device_frmpayload_data_counter_a
    # device_frmpayload_data_counter_b
    # device_frmpayload_data_payload_counter
    # device_frmpayload_data_sensor_status
    # device_frmpayload_data_total_counter_a
    # device_frmpayload_data_total_counter_b

    data = {
        "application_name": "abc123",
        "device_id": 'E8EB1BFF4F23',
        "device_uplink": {
            "rssi": 143
        },
        "measurement":{
            'device_status': 0,
            'battery_voltage': 2.41,
            'counter_a': 0,
            'counter_b': 0,
            'sensor_status': 162
        }
    }

    result = prepare_data(data)

    bucket = "TestBucket"
    write_points(client=client, bucket=bucket, org=org, sequence=result)
    # write_api = client.write_api(write_options=SYNCHRONOUS)

    # data = "mem,host=host1 used_percent=23.43234543"
    # write_api.write(bucket, org, data)


if __name__ == '__main__':
    main()
