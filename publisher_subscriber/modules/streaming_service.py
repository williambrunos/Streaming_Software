import redis

class StreamingService:
    """
    Class that implements a streaming service using
    pub sub architecture with Redis
    """
    def __init__(self, host, port, chanel):
        """
        Builder method
        
        Keyword arguments:
        argument host -- host of redis server
        argument port -- port of redis server
        argument chanel -- chanel to subscribe
        
        Return: object of StreamingService
        """
        
        self._redis_client = redis.Redis(host=host, port=port)
        self._pubsub = self._redis_client.pubsub()
        self._chanel = chanel
        self._pubsub.subscribe(self._chanel)
        
    def send_data(self, stream_id, data):
        """
        Method that sends data to a stream
        
        Keyword arguments:
        argument stream_id -- id of stream
        argument data -- data to send
        
        Return: N/A
        """
        
        message = f'{stream_id}:{data}'
        self._redis_client.publish(self._chanel, message)
        print(f'Sent data: {message}')
        
    def start_listening(self):
        """
        Method that starts listening to a stream
        
        Keyword arguments:
        argument N/A 
        
        Return: N/A
        """
        
        try:
            for message in self._pubsub.listen():
                if message['type'] == 'message':
                    stream_id, stream_data = message['data'].decode().split(':')
                    print('Received data: ', stream_id, stream_data)
        except KeyboardInterrupt:
            print('Stopped listening')
            
