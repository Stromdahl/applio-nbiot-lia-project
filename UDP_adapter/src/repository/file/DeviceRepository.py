def validate_device(device_id: str) -> bool:
	approved_devices = list()
	with open("../devices.txt") as device_file:
		for device in device_file:
			approved_devices.append(device)
	return device_id in approved_devices
