from socket import *
def requestClient(message: str):
    serverName = "localhost"
    serverPort = 12345
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    
    clientSocket.send(message.encode())
    modifiedSentence = clientSocket.recv(1024)
    
    clientSocket.close()
    return modifiedSentence.decode()
