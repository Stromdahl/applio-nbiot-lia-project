from log import Log
from server_connection import ServerSocket
from config import Config

from log import Log
from translater import decode
from Devices.devicetype2variant4 import DeviceType2Variant4
from repository.file.DeviceRepository import validate_device

log = Log("server")


class Server(ServerSocket):

	def handle_incoming_message(self, address: tuple[str, int], payload: str) -> None:
		data = decode(payload)
		device = DeviceType2Variant4(**data)
		approved = "Approved" if validate_device(device.device_id) else "Denied"
		log.debug(f"Device: {device} {approved}")


def main():

	log.info(f"Starting server on {Config.ADDRESS}:{Config.PORT}...")
	server = Server(address=Config.ADDRESS, port=Config.PORT)
	server.run()


if __name__ == '__main__':
	main()
