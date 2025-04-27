import socket
import threading


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print(f"接收到服务端消息: {data.decode()}")
            else:
                # Connection closed
                break
        except Exception as e:
            print(f"接收服务端消息失败: {e}")
            break


def send_message(sock):
    while True:
        message = input("输入消息，回车发送: ")
        try:
            sock.sendall(message.encode())
        except Exception as e:
            print(f"消息发送失败: {e}")
            break


def main():
    pass


if __name__ == "__main__":
    main()
