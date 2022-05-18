from log import Log
import socket
from config import Config

from messages import MessageHandler


# Todo: implement check if able to bind to a address and port
# Todo: implement ipv6 for udp
# Todo: make async...


class UDPTransportInterface:
	"""
	Handles the listening for incoming udp messages,
	Requires
		- socket
		- log
		- callable message_handler with parameters address: tuple[str, int] and payload: str
	"""
	# Todo: update documentation

	def __init__(self, sock, log, message_handler: MessageHandler):
		self.sock = sock
		self.log = log
		self.buffer_size = 1024
		self.message_handler = message_handler

	def run(self) -> None:
		"""
		main loop for incoming message handling
		"""

		while True:
			bytes_address_pair = self.sock.recvfrom(self.buffer_size)
			payload = bytes_address_pair[0]
			address = bytes_address_pair[1]

			self.message_handler.message(address, payload=payload.decode("utf-8"))

	@classmethod
	def create_server_transport_interface(cls, bind, log, message_handler: MessageHandler):
		"""
		Creates the interface for incoming messages
		Requires
		- context
		- callable message_handler with parameters address: tuple[str, int] and payload: str
		"""

		sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		sock.bind(bind)

		return cls(sock, log, message_handler)


class Context:

	def __init__(self, interface: UDPTransportInterface, log: Log):
		self.interface = interface
		self.log = log
		self.buffer_size = 1024

	@classmethod
	def create_server_context(cls, message_handler: MessageHandler, bind: tuple[str, int] = None,
							  loggername: str = "message"):
		bind = bind or (Config.ADDRESS, None)
		bind = (bind[0], Config.PORT if bind[1] is None else bind[1])

		log = Log(loggername)

		udp_transport_interface = UDPTransportInterface.create_server_transport_interface(bind=bind, log=log,
																						  message_handler=message_handler)

		self = cls(interface=udp_transport_interface, log=log)

		return self

	def run(self):
		self.interface.run()
