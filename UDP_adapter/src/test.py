import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("test/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))


def on_publish(client, userdata, result):
	print("Data published...")


def main():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_publish = on_publish

#	client.connect("mqtt.eclipseprojects.io", 1883, 60)

	client.connect("127.0.0.1", 1883, 60)
	ret = client.publish("test/python")

	# Blocking call that processes network traffic, dispatches callbacks and
	# handles reconnecting.
	# Other loop*() functions are available that give a threaded interface and a
	# manual interface.
	client.loop_forever()


if __name__ == '__main__':
	main()
