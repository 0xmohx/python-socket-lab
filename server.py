# to run this code : python3 server.py --port 4444
import socket
from threading import Thread
import click

def handle_client(client, addr):
    print(f"[+] Client connected: {addr}")

    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            message = data.decode().strip()
            print(f"[CLIENT] {addr}: {message}")

            if message.lower() == "exit":
                client.send(b"Goodbye!\n")
                break

            response = f"Server received: {message}"
            client.send(response.encode())

        except:
            break

    client.close()


@click.command()
@click.option("--host", default="0.0.0.0", help="Bind address")
@click.option("--port", default=4444, help="Port to listen on")
def main(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[+] Listening on {host}:{port}")

    while True:
        client, addr = server.accept()
        thread = Thread(target=handle_client, args=(client, addr))
        thread.start()


if __name__ == "__main__":
    main()
