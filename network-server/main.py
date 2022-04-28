import json

import paho.mqtt.client as mqtt

from DeviceAPI import get_device


def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
    device = json.loads(message.payload.decode('utf-8'))
    application_name = get_device(device['device_id'])
    if application_name:
        device["application_name"] = application_name
        print(f"{message.topic}, {str(device)}")
        client.publish(f"gateway/{device['device_id']}", payload=json.dumps(device))


def main():
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.subscribe("adapter/#")

    client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    main()
