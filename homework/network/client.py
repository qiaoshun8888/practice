# import socket module
import sys
from socket import *
from datetime import datetime
from threading import Thread


class ConnectionThread(Thread):

    def __init__(self, connectionSocket):
        super(ConnectionThread, self).__init__()
        self.connectionSocket = connectionSocket

    def run(self):
        connectionSocket = self.connectionSocket
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            with open(filename[1:], 'r') as f:
                outputdata = f.read()
            # Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\r\n')
            connectionSocket.send("Content-Type: text/html\r\n\r\n")
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
        except IOError:
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n')
            connectionSocket.send("Content-Type: text/html\r\n\r\n")
            with open('404.html', 'r') as f:
                connectionSocket.send(f.read())
            # Send response message for file not found
            # Close client socket
            connectionSocket.close()
        except:
            pass


def main(*args):
    print args
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    HOST = '127.0.0.1'
    PORT = 6789
    serverSocket.connect((HOST, PORT))
    s.send
    serverSocket.close()

if __name__ == '__main__':
    main(*sys.argv)
