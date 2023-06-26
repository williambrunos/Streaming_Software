import socket

class StreamingClient:
    def __init__(self, host, port):
        """
        Builder method.
        
        Keyword arguments:
        argument host -- The host of the server
        argument port -- The port of the server
        
        Return: Object of type StreamingClient
        """
        
        self._host = host
        self._port = port
        
    def send_data(self, stream_id, data):
        """
        Method responsible for sending the data to host in the
        specified port.
        
        Keyword arguments:
        argument stream_id -- The stream id to send the data
        argument data -- The data to send
        
        Return: N/A
        """
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self._host, self._port))
        
        message = f'{stream_id}:{data}'
        message_length = len(message).to_bytes(4, byteorder='big')
        prefixed_message = message_length + message.encode()
        
        client_socket.sendall(prefixed_message)
        print(f'Sent {prefixed_message}, {type(prefixed_message)}')
        client_socket.close()
        
        
def main():
    SERVER_RUNNING_PORT = 8000
    client = StreamingClient('localhost', SERVER_RUNNING_PORT)
    client.send_data('stream1', 'data1')
    client.send_data('stream1', 'data2')

if __name__ == '__main__':
    main()
