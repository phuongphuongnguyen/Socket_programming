from socket import *
def requestClient(message: str):
    serverName = "localhost"
    serverPort = 12345
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    clientSocket.close()
    return modifiedMessage.decode()