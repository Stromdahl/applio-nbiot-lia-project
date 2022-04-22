import paho.mqtt.client as mqtt
import random


def on_message(client, userdata, message):
    print(f"{message.topic}, {str(message.payload.decode('utf-8'))}")


def main():
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.publish("test/abc", payload=random.randint(0, 100))
    client.subscribe("adapter/#")

    client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    main()
