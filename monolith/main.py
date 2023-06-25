class StreamingService:
    """
    This class is responsible for managing streams and their data.
    """
    
    def __init__(self):
        """
        Builder method.
        
        Keyword arguments:
        argument N/A
        
        Return: Object of type StreamingService
        """
        
        self._streams = {}
        
    def add_stream(self, stream_id):
        """
        Function responsible for adding a stream.
        
        Keyword arguments:
        argument stream_id -- The id of the stream to be added
        
        Return: N/A
        """
        
        if stream_id not in self._streams:
            self._streams[stream_id] = []
            print(f"Stream {stream_id} added")
        else:
            print(f"Stream {stream_id} already exists")
            
    def add_data_to_stream(self, stream_id, data):
        """
        Function responsible for adding data to a specific stream
        according to its id.
        
        Keyword arguments:
        argument stream_id -- The id of the stream to add data to
        argument data -- The data to be added to the stream
        
        Return: N/A
        """
        
        if stream_id in self._streams:
            self._streams[stream_id].append(data)
            print(f"Stream {stream_id} added data {data}")
        else:
            print(f"Stream {stream_id} does not exist")
    
    def get_stream_data(self, stream_id):
        """
        Function responsible for returning the data of a specific stream
        according to its id.
        
        Keyword arguments:
        argument stream_id -- The id of the stream to get data from
        
        Return: The list of data stored on the stream
        """
        
        if stream_id in self._streams:
            return self._streams[stream_id]
        else:
            print(f"Stream {stream_id} does not exist")
            return None
        
        
def main():
    streaming_service = StreamingService()
    streaming_service.add_stream('stream1')
    streaming_service.add_data_to_stream('stream1', 'data1')
    streaming_service.add_data_to_stream('stream1', 'data2')
    
    print(f'Stream data: {streaming_service.get_stream_data("stream1")}')
    

if __name__ == '__main__':
    main()
