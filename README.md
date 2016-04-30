## Calculator

### What is this?
A simple demo of communication between server and client using gevent and protobuf
### How to use?
- start the server

    	python server.py
- sending message using client

   		python client.py '( ( 3 + 4 ) * 2 * 100 )'

### Examples

client side

    # python client.py '( ( 3 + 4 ) * 2 * 100 )'
    connecting...
    sending messages...
    200

server side

    # python server.py
    Got one task from client: ( ( 3 + 4 ) * 2 * 100 )

### Note
- the expression sent from the client to server to compute must be splitted with white spaces and parenthesises are required as necessary, see examples from above.
