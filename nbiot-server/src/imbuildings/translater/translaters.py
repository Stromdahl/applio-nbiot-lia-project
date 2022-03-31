from abc import ABC, abstractmethod


class PayloadTranslater(ABC):
    @abstractmethod
    def decode(self, payload: bytearray) -> dict:
        ...

    @abstractmethod
    def encode(self, data: dict) -> bytearray:
        ...


class Type2Variant4(PayloadTranslater):
    def decode(self, payload: bytearray) -> dict:
        return {
            'payload_type': 2,
            'payload_variant': 4,
            'device_id': payload[2:8].hex().upper(),
            'device_status': payload[8],
            'battery_voltage': int.from_bytes(payload[9:11], "big") / 100.,
            'rssi_level': payload[11],
            'date': payload[12:16].hex(),
            'time': payload[16:19].hex(),
            'counter_a': int.from_bytes(payload[19:21], "big"),
            'counter_b': int.from_bytes(payload[21:23], "big"),
            'sensor_status': payload[23]
        }

    def encode(self, data: dict) -> bytearray:
        payload = bytearray()
        payload.append(data['payload_type'])
        payload.append(data['payload_variant'])
        payload.extend(bytearray.fromhex(data['device_id']))
        payload.append(data['device_status'])
        payload.extend(int(data['battery_voltage'] * 100).to_bytes(2, 'big'))
        payload.append(data['rssi_level'])
        payload.extend(bytearray.fromhex(data['date']))
        payload.extend(bytearray.fromhex(data['time']))
        payload.extend(data['counter_a'].to_bytes(2, 'big'))
        payload.extend(data['counter_b'].to_bytes(2, 'big'))
        payload.append(data['sensor_status'])
        return payload


class Type2Variant6(PayloadTranslater):
    def decode(self, payload: bytearray) -> dict:
        return {
            "payload_type": 2,
            "payload_variant": 6,
            "device_id": payload[2:10].hex().upper(),
            "device_status": payload[10],
            "battery_voltage": int.from_bytes(payload[11:13], "big") / 100.,
            "counter_a": int.from_bytes(payload[13:15], "big"),
            "counter_b": int.from_bytes(payload[15:17], "big"),
            "sensor_status": payload[17],
            "total_counter_a": int.from_bytes(payload[18:20], "big"),
            "total_counter_b": int.from_bytes(payload[20:22], "big"),
            "payload_counter": payload[22]
        }

    def encode(self, data: dict) -> bytearray:
        payload = bytearray()
        payload.append(data['payload_type'])
        payload.append(data['payload_variant'])
        payload.extend(bytearray.fromhex(data['device_id']))
        payload.append(data['device_status'])
        payload.extend(int(data['battery_voltage'] * 100).to_bytes(2, 'big'))
        payload.extend(data['counter_a'].to_bytes(2, 'big'))
        payload.extend(data['counter_b'].to_bytes(2, 'big'))
        payload.append(data['sensor_status'])
        payload.extend(data['total_counter_a'].to_bytes(2, 'big'))
        payload.extend(data['total_counter_b'].to_bytes(2, 'big'))
        payload.append(data['payload_counter'])
        return payload


class TranslaterFactory:
    def __init__(self):
        self._translators = dict()

    def register_translater(self, payload_type: int, payload_variant: int, translater):
        self._translators[payload_type, payload_variant] = translater

    def get_translater(self, payload_type: int, payload_variant: int) -> PayloadTranslater:
        translater = self._translators[payload_type, payload_variant]
        if not translater:
            raise ValueError(format)
        return translater()
