import socket
from abc import ABC, abstractmethod


class ServerSocket(ABC):
	"""Base class for the server socket handling"""
	def __init__(self, address: str, port: int):
		self.address = address
		self.port = port
		self.buffer_size = 1024

	def run(self) -> None:
		# Create a datagram socket
		udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		udp_server_socket.bind((self.address, self.port))

		while True:
			bytes_address_pair = udp_server_socket.recvfrom(self.buffer_size)
			payload = bytes_address_pair[0]
			address = bytes_address_pair[1]

			self.handle_incoming_message(payload.decode("utf-8"))

	@abstractmethod
	def handle_incoming_message(self, address: tuple[str, int], payload: str) -> None:
		"""Responsible for handling the incoming messages to the server"""
		...