from modules.streaming_service import StreamingService


def main():
    streaming_service = StreamingService('localhost', 'streaming')
    streaming_service.send_data('1', 'Hello world!')
    streaming_service.send_data('2', 'Hello world!')
    streaming_service.start_listening()
    
    
if __name__ == '__main__':
    main()
