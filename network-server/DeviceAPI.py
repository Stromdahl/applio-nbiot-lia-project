
devices = {
	"FF00FF": "abcd12345",
	"0004A30B00F6": "aegasg1324da"
}


def get_device(device_name: str):
	try:
		return devices[device_name]
	except KeyError:
		return None
