# to run this code: python3 client.py --host 127.0.0.1 --port 4444
import socket
import click

@click.command()
@click.option("--host", default="127.0.0.1", help="Server IP")
@click.option("--port", default=4444, help="Server port")
def main(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("[+] Connected")

    while True:
        msg = input("You: ")

        client.send(msg.encode())
        response = client.recv(1024).decode()

        print(f"Server: {response}")

        if msg.lower() == "exit":
            break

    client.close()


if __name__ == "__main__":
    main()
