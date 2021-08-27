# Implement Chat Application.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import time
import socket


if __name__ == '__main__':
    print("\nWelcome to Chat Room\n")
    time.sleep(1)

    s = socket.socket()
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 1234
    s.bind((host, port))
    print(host, "(", ip, ")\n")
    name = input(str("Enter your name: "))

    s.listen(1)
    print("\nWaiting for incoming connections...\n")
    connect, address = s.accept()
    print("Received connection from ", address[0], "(", address[1], ")\n")

    s_name = connect.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has connected to the chat room\nEnter [1] to exit chat room\n")
    connect.send(name.encode())

    while True:
        message = input(str("Me : "))
        if message == "1":
            message = "Left chat room!"
            connect.send(message.encode())
            print("\n")
            break
        connect.send(message.encode())
        message = connect.recv(1024)
        message = message.decode()
        print(s_name, ":", message)