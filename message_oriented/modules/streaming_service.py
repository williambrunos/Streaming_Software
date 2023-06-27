import pika

class StreamingService:
    """
    Class that implements a streamming service using message broker
    and message oriented architecture.
    """
    def __init__(self, host, quee_name):
        """
        Builder of the class.
        
        Keyword arguments:
        argument host -- host of the broker server
        argument queue_name -- name of the queue
        
        return objet: StreamingService
        """
        
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self._chanel = self._connection.channel()
        self._chanel.queue_declare(queue=quee_name)
        
    def send_data(self, stream_id, data, routing_key='streaming'):
        """
        Method that sends data to a stream.
        
        Keyword arguments:
        argument stream_id -- id of the stream
        argument data -- data to be sent
        argument routing_key -- routing key of the queue
        
        Return: N/A
        """
        
        message = f'{stream_id}:{data}'
        self._chanel.basic_publish(exchange='', routing_key=routing_key, body=message)

        print(f'Sent data to stream {stream_id}: {data}')
        
    def _process_data(self, chanel, method, properties, body):
        """
        Method that process data received from a stream.
        
        Keyword arguments:
        argument chanel -- chanel of the queue
        argument method -- method of the queue
        argument properties -- properties of the queue
        argument body -- body of the queue
        
        Return: N/A
        """
        
        stream_id, data = body.decode().split(':', 1)

        print(f'Received data from stream {stream_id}: {data}')
        
    def start_listening(self, routing_key='streaming'):
        """
        Method that starts listening to a stream.
        
        Keyword arguments:
        argument routing_key -- routing key of the queue
        
        Return: N/A
        """
        
        self._chanel.basic_consume(queue=routing_key, on_message_callback=self._process_data, auto_ack=True)
        print('Waiting for messages...')
        try:
            self._chanel.start_consuming()
        except KeyboardInterrupt:
            print('Stopped listening')
            self._connection.close()
