# Python-Socket-Connection
Creates a socket connection between two machines on port 8080.

The main client creates a socket on port 8080 and listens for a response from the remote client.
The remote client attempts to connect to the port 8080 but the ip address must be configured to the host client.
To connect to remote clients outside your local network you can use something such as ngrok to create a TCP/IP connection that points to port 8080 using the host machines ip address. 

