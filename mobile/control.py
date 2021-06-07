import socket
import time
import requests

lights=""


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
print("Checking local network for lights...")
data, addr = client.recvfrom(1024)
data=str(data,"utf-8")
parts=data.split("/")
if parts[0]=="mrslight":
    lights=parts[1]
print("Found a light: "+lights)


while True:

    a=input("Enter ON, OFF, RED, GREEN or BLUE. More colours coming soon: ")
    a=a.strip()
    if a=="ON":
        payload = {'r':'255','g':'255','b':'255'}
    elif a=="OFF":
        payload = {'r':'0','g':'0','b':'0'}
    elif a=="RED":
        payload = {'r':'255','g':'0','b':'0'}
    elif a=="GREEN":
        payload = {'r':'0','g':'255','b':'0'}
    elif a=="BLUE":
        payload = {'r':'0','g':'0','b':'255'}
    else:
        print("That isn't implemented")
        continue
    payload["mac"]=lights
    r = requests.post('http://174.27.0.20/index.php',data=payload)
    #print(r.text)
    time.sleep(3)
