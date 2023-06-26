import socket
import threading

class StreamingService:
    def __init__(self, host, port):
        """
        Builder method.
        
        Keyword arguments:
        argument host -- The host of the server
        argument port -- The port of the server
        
        Return: Object of type StreamingService
        """
        
        self._host = host
        self._port = port
        self._streams = {}
        
    def start(self):
        """
        Function responsible for starting the server.
        
        Keyword arguments:
        argument N/A
        
        Return: N/A
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self._host, self._port))
        server_socket.listen()
        self._server_runnig = True
        
        print(f'Server listening on {self._host}:{self._port}')
        
        while True:
            client_socket, address = server_socket.accept()
            print(f'Client connected from {address}')
                            
            client_handler = ClientHandler(client_socket, self._streams)
            client_handler.start()
            
            
class ClientHandler(threading.Thread):
    def __init__(self, client_socket, streams):
        """
        Builder method.
        
        Keyword arguments:
        argument client_socket -- The socket of the client
        argument socket -- The socket of the server
        argument streams -- The streams of the server
        
        Return: Object of type ClientHandler
        """
        
        threading.Thread.__init__(self)
        self._client_socket = client_socket
        self._streams = streams
    
    def run(self):
        """
        Function responsible for running the thread.
        
        Keyword arguments:
        argument N/A
        
        Return: N/A
        """
        
        while True:
            data = self.receive_message()
            print(f'Received {data}')
            if not data:
                break
            
            data = data.decode()
            # 1013:stream1:data1
            stream_id, stream_data = data[4:].split(':', 1)
            if stream_id not in self._streams:
                self._streams[stream_id] = []
            self._streams[stream_id].append(stream_data)
            
        self._client_socket.close()
        
    def receive_message(self):
        """
        Method responsible for receiving the message.
        
        Keyword arguments:
        argument N/A 
        Return: data read from the socket
        """
        
        message_length = self._client_socket.recv(4)
        if not message_length:
            return b''
        
        message_length = int.from_bytes(message_length, byteorder='big')
        return self.receive_data(message_length)
    
    def receive_data(self, length):
        """
        Receive data from the socket and returns the data
        read after a certain amount of bytes specified
        as prefix of the message.
        
        Keyword arguments:
        argument length -- length of the message in bytes
        Return: data -- data read from the socket
        """
        
        data = b''
        while len(data) < length:
            packet = self._client_socket.recv(length - len(data))
            if not packet:
                return b''
            data += packet
        
        return data
    
def main():
    SERVER_RUNNING_PORT = 8000
    
    server = StreamingService('localhost', SERVER_RUNNING_PORT)
    server.start()
    
    
if __name__ == '__main__':
    main()
    