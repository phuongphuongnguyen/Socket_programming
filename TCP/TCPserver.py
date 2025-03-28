from socket import *

def runServer(update_gui):
    serverPort = 12345
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)  

    print("The server is ready to receive")
   
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()

        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
        update_gui(sentence, capitalizedSentence)

