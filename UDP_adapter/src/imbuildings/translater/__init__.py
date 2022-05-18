from .translaters import TranslaterFactory, Type2Variant4, Type2Variant6

factory = TranslaterFactory()
factory.register_translater(payload_type=2, payload_variant=4, translater=Type2Variant4)
factory.register_translater(payload_type=2, payload_variant=6, translater=Type2Variant6)


def decode(payload: str) -> dict:
	payload_bytes = bytearray.fromhex(payload)
	translater = factory.get_translater(payload_bytes[0], payload_bytes[1])
	return translater.decode(payload_bytes)


def encode(data: dict) -> bytearray:
	translater = factory.get_translater(data['payload_type'], data['payload_variant'])
	return translater.encode(data)
