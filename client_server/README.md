## Client server implementation

The codes `server.py` and `client.py` implements the server and client services in this architecture.

### About the server

The server is implemented in a way that it constantly receives data from the client using **TCP** protocol and **socket** python package.
Because of the usage of TCP protocol, the message boundaries wouldn't be respected by the socket package. Because of that, two functions, called `receive_message` and `receive_data` are created to receive the message using a 4 bytes prefix that indicates the length of the message. The message with the 4 bytes prefix is read in the `receive_message` method to calculate the lenght of the message sent by the client. After that, the data itself is read by the `receive_data` method, ensuring that TCP protocol does not read and returns empty byte strings.

**OBS**: even with this implementations, the server will read a empty byte string when the client socket is closed in the `client.py` code.

### About the client

The client is implemented in a way that it will send a 4 bytes prefix in the message to the server to indicate the length of the message sent. This will help the socket implemented with TCP protocol to not receive or return any unnecessary empty byte string due to boundaries "disrespect" of TCP protocol.

## How to run the codes

First, navigate to the *client_server* folder

````Bash
cd client_server/
````

After that, run the `server.py` and `client.py` codes

````Bash
python server.py
python client.py
````