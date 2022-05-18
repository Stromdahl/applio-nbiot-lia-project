from dataclasses import dataclass


@dataclass
class DeviceType2Variant4:
	device_id: str
	device_status: int
	battery_voltage: float
	rssi_level: int
	date: str
	time: str
	counter_a: int
	counter_b: int
	sensor_status: int
	payload_type: int = 2
	payload_variant: int = 4

	def __repr__(self):
		return f'{self.device_id}'
