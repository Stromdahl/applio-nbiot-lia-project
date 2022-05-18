from transport import Context
from messages import MessageType, MessageHandler
from config import Config
from log import Log
from imbuildings.translater import decode
import paho.mqtt.client as mqtt
import json
log = Log("server")

client = mqtt.Client()


class Message(MessageType):
	def handle_message(self, address: tuple[str, int], payload: str):
		data = decode(payload)

		log.debug(f"Device {data['device_id']} sent a {len(payload)//2} byte package")
		client.publish(f"adapter/UDP/{data['device_id']}", payload=json.dumps(data))
		pass


def main():
	client.connect("localhost", 1883, 60)

	# Create a MessageHandler
	message_handler = MessageHandler()

	# Add a message type
	message_handler.add_message_type(Message())

	log.info(f"UDP adapter started on: {Config.ADDRESS}:{Config.PORT}...")
	context = Context.create_server_context(message_handler)
	context.run()


if __name__ == '__main__':
	main()
