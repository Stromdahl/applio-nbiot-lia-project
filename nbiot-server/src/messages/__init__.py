from abc import ABC, abstractmethod


class MessageType(ABC):

	@abstractmethod
	def handle_message(self, address: tuple[str, int], payload: str):
		...


class MessageHandler:
	_message_types: list[MessageType] = []

	def add_message_type(self, message_type: MessageType):
		self._message_types.append(message_type)

	def message(self, address: tuple[str, int], payload: str):
		for message_type in self._message_types:
			message_type.handle_message(address, payload)