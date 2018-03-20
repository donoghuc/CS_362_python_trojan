# Toy "trojan" demo for CS373 final project
This repository contains a code demo for a my final report presentation in CS373 Defense Against the Dark Arts at Oregon State university. The report topic is on trojan malware. This code base is HARMLESS it is just used to demonstrate how a simple command and control server can take control of computer using a hidden payload. 

This example is based off https://github.com/alexAubin/evilBunnyTrojan

## Installation/Requirements 
- Clone entire repository or download just the evil_bunny_server.py and evil_bunny_trojan.py source files
- Ensure python 3 installed (I am using Python 3.6.3 :: Anaconda, Inc) from the miniconda distribution

## Demo
### open up two terminals
- One terminal will run the "evil" server and the other will run the trojan
- Note I print out the python version and directory structure
![two_terms](img/two_terms.png?raw=true "two_terms")

### start the server
``` python evil_bunny_server.py ```
![start_server](img/start_server.png?raw=true "start_server")

### start the trojan
- The "bunny" that will keep "dancing" in the trojan terminal represents the process that the victim would think was useful. 
- For clarity I print out a bunch of info on the "trojan" side for the purpose of showing what is happening. 
``` python evil_bunny_trojan.py ```
![start_trojan](img/start_trojan.png?raw=true "start_trojan")

### command and control
- shell commands can be issued from the control server. 
- Syntax is to type run followed by comma separated shell commands
- For example: run,ls,-pla
- Command status is returned to server 
EVIL SERVER
```
cas@ubuntu:~/working_dir/DADA/CS373_python_trojan$ python evil_bunny_server.py 
Server listening on port 8912
Connected with 127.0.0.1: 45408
Command to target: run,ls,-pla
last command status: 0
```
TROJAN CLIENT
```
[Server] run,ls,-pla
total 24
drwxr-xr-x 4 cas cas 4096 Mar 20 12:30 ./
drwxr-xr-x 4 cas cas 4096 Mar 20 12:24 ../
-rw-r--r-- 1 cas cas 1750 Mar 20 12:18 evil_bunny_server.py
-rw-r--r-- 1 cas cas 2363 Mar 20 12:18 evil_bunny_trojan.py
drwxr-xr-x 8 cas cas 4096 Mar 20 12:31 .git/
drwxr-xr-x 2 cas cas 4096 Mar 20 12:52 img/
-rw-r--r-- 1 cas cas    0 Mar 20 12:26 README.md
```
![run_ls](img/run_ls.png?raw=true "run_ls")

### commands for video demo
```
run,ls,-pla
run,curl,-LO,https://github.com/donoghuc/CS_362_python_trojan/raw/master/img/The_Rabbit_of_Caerbannog.jpg
run,ls,-pla
run,xdg-open,The_Rabbit_of_Caerbannog.jpg
run,rm,The_Rabbit_of_Caerbannog.jpg
run,ls,-pla
```
