import time
import socket
import random
from src.imbuildings.translater import encode
from src.log import Log


class Client:
    def __init__(self, address: str, port: int) -> None:
        self.address = address
        self.port = port
        self.udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def send_payload(self, payload: bytes) -> None:
        self.udp_client_socket.sendto(payload, (self.address, self.port))


def main():
    log = Log("client")

    data = {
        'payload_type': 2,
        'payload_variant': 4,
        'device_id': '0004A30B00F6',
        'device_status': 8,
        'battery_voltage': 2.48,
        'rssi_level': 2,
        'date': '20220310',
        'time': '114422',
        'counter_a': 0,
        'counter_b': 0,
        'sensor_status': 32,
    }

    client = Client("127.0.0.1", 20001)

    while True:
        t = time.localtime()
        data['date'] = time.strftime('%Y%m%d', t)
        data['time'] = time.strftime('%H%M%S', t)

        data['counter_a'] = random.randint(0, 5)
        data['counter_b'] = random.randint(0, 5)

        payload = encode(data).hex()

        log.info(payload)

        payload_bytes = str.encode(payload)

        client.send_payload(payload_bytes)

        time.sleep(2)


if __name__ == "__main__":
    main()
