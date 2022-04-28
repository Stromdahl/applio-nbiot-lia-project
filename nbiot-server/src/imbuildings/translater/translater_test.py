import unittest

from .translaters import Type2Variant4, Type2Variant6


class TestType2Variant4(unittest.TestCase):
    def setUp(self):
        self.payload = bytearray.fromhex("02040004A30B00F60800F802202203101144220003000220")
        self.data = {
            "payload_type": 2,
            "payload_variant": 4,
            "device_id": "0004A30B00F6",
            "device_status": 8,
            "battery_voltage": 2.48,
            "rssi_level": 2,
            "date": "20220310",
            "time": "114422",
            "counter_a": 3,
            "counter_b": 2,
            "sensor_status": 32,
        }

    def test_decoder(self):
        self.assertDictEqual(Type2Variant4().decode(self.payload), self.data)

    def test_encoder(self):
        self.assertEquals(Type2Variant4().encode(self.data), self.payload)


class TestType2Variant6(unittest.TestCase):
    def setUp(self):
        self.payload = bytearray.fromhex("02060004A30B00F6B5690800F80003000220060305E661")
        self.data = {
            "payload_type": 2,
            "payload_variant": 6,
            "device_id": "0004A30B00F6B569",
            "device_status": 8,
            "battery_voltage": 2.48,
            "counter_a": 3,
            "counter_b": 2,
            "sensor_status": 32,
            "total_counter_a": 1539,
            "total_counter_b": 1510,
            "payload_counter": 97,
        }

    def test_decoder(self):
        self.assertDictEqual(Type2Variant6().decode(self.payload), self.data)

    def test_encoder(self):
        self.assertEquals(Type2Variant6().encode(self.data), self.payload)