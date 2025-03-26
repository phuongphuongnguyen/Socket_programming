from socket import *

def runServer(update_gui):
    serverPort = 12345
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("", serverPort))

    print("The server is ready to receive")
   
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        received_text = message.decode()
        modifiedMessage = received_text.upper()

        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        
        update_gui(received_text, modifiedMessage)



