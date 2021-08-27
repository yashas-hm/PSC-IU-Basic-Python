# Implement Chat Application.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066

import time
import socket


if __name__ == '__main__':
    print("\nWelcome to Chat Room\n")
    time.sleep(1)

    s = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    print(shost, "(", ip, ")\n")
    host = input(str("Enter server address: "))
    name = input(str("\nEnter your name: "))
    port = 1234
    print("\nTrying to connect to ", host, "(", port, ")\n")
    time.sleep(1)
    s.connect((host, port))
    print("Connected...\n")

    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has joined the chat room\nEnter [1] to exit chat room\n")

    while True:
        message = s.recv(1024)
        message = message.decode()
        print(s_name, ":", message)
        message = input(str("Me : "))
        if message == "1":
            message = "Left chat room!"
            s.send(message.encode())
            print("\n")
            break
        s.send(message.encode())
