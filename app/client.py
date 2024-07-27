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
    host = 'customer.saas.idtest.bowenfin.com'
    port = 80
    path = '/?loginUserNum=123123&appinfoId=1000'

    try:
        # Debugging: Print the hostname to check
        print(f"远程 host: {host}")

        # Resolve the hostname to an IP address
        ip_address = socket.gethostbyname(host)
        print(f"host：{host} is {ip_address}")

        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        sock.connect((ip_address, port))

        # Send HTTP GET request
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: keep-alive\r\n\r\n"
        sock.sendall(request.encode())

        # Start a thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(sock,))
        receive_thread.start()

        # Main thread to send messages
        send_message(sock)

    except socket.gaierror as e:
        print(f"Unable to resolve the server: {e}")
    except Exception as e:
        print(f"Unable to connect to the server: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
