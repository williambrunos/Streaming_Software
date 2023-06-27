from modules.streaming_service import StreamingService

def main():
    streaming_service = StreamingService('localhost', '6379', 'stream_chanel')
    streaming_service.send_data('stream_1', 'Hello world!')
    streaming_service.send_data('stream_1', 'Hello world!')
    streaming_service.start_listening()
    

if __name__ == '__main__':
    main()
    