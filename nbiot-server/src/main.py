from transport import Context
from messages import MessageType, MessageHandler
from config import Config
from log import Log
from imbuildings.translater import decode
from imbuildings.Devices.devicetype2variant4 import DeviceType2Variant4
from repository.file.DeviceRepository import validate_device

log = Log("server")

# Todo: Influx integration...


class Message(MessageType):
	def handle_message(self, address: tuple[str, int], payload: str):
		data = decode(payload)
		device = DeviceType2Variant4(**data)
		approved = "Approved" if validate_device(device.device_id) else "Denied"
		log.debug(f"Device: {device} {approved}")


def main():
	message_handler = MessageHandler()
	message_handler.add_message_type(Message())

	log.info(f"Starting server on {Config.ADDRESS}:{Config.PORT}...")
	context = Context.create_server_context(message_handler)
	context.run()


if __name__ == '__main__':
	main()
