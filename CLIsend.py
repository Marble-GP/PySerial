import socket
import threading
from time import sleep

def sending(sock, mode, addr, port, data):
    while bool(mode):
        sock.sendto(data, (addr, port))
        sleep(0.001)


if __name__ == "__main__":
    print("**** this is only UDP ****")
    addr = input("address:")
    port = int(input("port:"))
    mode = int(input("mode( 0=oneshot, other=loop) :"))
    data = eval(input("data(bytes format, ef. b\"\\xFF\\xAB\\x00\" ) :"))
    print("data = {}".format(data))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    sock.sendto(data, (addr, port))
    data = sock.recv(0xFFFF)
    print(data)
    sleep(0.001)
    while True:
        if mode:
            sock.sendto(data, (addr, port))
        data = sock.recv(0xFFFF)
        print(data)
        sleep(0.001)
        