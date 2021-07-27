import socket
from threading import Thread
import json

from sound import Sound

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)


    def listen_for_clients(self):
        print('Listening...')
        while True:
            client, addr = self.server.accept()
            print(
                'Accepted Connection from: ' + str(addr[0]) + ':' + str(addr[1])
            )
            Thread(target=self.handle_client, args=(client, addr)).start()

    def handle_client(self, client_socket, address):
        global sound
        sound = Sound()
        size = 1024
        while True:
            try:
                data = client_socket.recv(size)
                if 'q^' in data.decode():    
                    print('Received request for exit from: ' 
                            + str(address[0]) + ':' + str(address[1]))
                    client_socket.sendall('q^\n'.encode())
                    sound.quit()
                    break

                else:
                    # send getting after receiving from client
                    client_socket.sendall('Welcome to server\n'.encode())

                    print('Received: ' + data.decode() + ' from: ' 
                            + str(address[0]) + ':' + str(address[1]))
                    # Json Decoder
                    try:
                        json_data = json.loads(data.decode())
                        for li in json_data:
                            if li.get("text") is not None:
                                sound.speak(li["text"])
                            if li.get("setting") is not None:
                                if li.get("setting").get("volume") is not None:
                                    sound.setting(volume=li["setting"]["volume"])
                                if li.get("setting").get("rate") is not None:
                                    sound.setting(rate=li["setting"]["rate"])
                    except json.JSONDecodeError as e:
                        print("ERROR: json.JSONDecodeError")

            except socket.error:
                sound.quit()
                client_socket.close()
                return False

        client_socket.sendall(
            'Received request for exit. Deleted from server threads'.encode()
        )

        # send quit message to client too
        client_socket.sendall(
            'q^'.encode()
        )
        client_socket.close()


if __name__ == "__main__":
    # host = socket.gethostname()   # 192.168.1.7
    # host = '127.0.0.1'
    host = '192.168.1.7'
    port = 5010
    main = Server(host, port)
    # start listening for clients
    main.listen_for_clients()

