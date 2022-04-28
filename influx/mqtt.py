#SUB

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected...")


def on_message(client, userdata, msg):
    print(f"Message received [{msg.topic}]: {msg.payload}")


def main():
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)

    client.subscribe("adapter/#")
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    main()
    pass


'''
# PUBLISH

import paho.mqtt.client as paho

def on_publish(client, userdata, result):  # create function for callback
    print("message sent")
    pass

client1 = paho.Client()  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.connect("localhost", 1883, 60)  # establish connection
client1.publish("adapter/test", payload="hejhej")  # publish

#Mattias
def on_message(client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
    device = json.loads(message.payload.decode('utf-8'))
    application_name = get_device(device['device_id'])
    response = get_device(device['device_id'])
    if response:
        device["application_name"] = application_name
        print(f"{message.topic}, {str(device)}")
        client.publish(f"gateway/{device['device_id']}", payload=json.dumps(device))

'''