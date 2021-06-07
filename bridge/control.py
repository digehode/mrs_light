import socket
import time
from colr import color
import requests
import json
import base64

mac="16:21:C9:A1:EC:DD"

def localMacPublish():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = str.encode("mrslight/%s"%(mac))


    server.sendto(message, ('255.255.255.255', 37020))

r,g,b=0,0,0

while True:
    localMacPublish()
    resp = requests.get('http://174.27.0.20/index.php',params={"mac":mac})
    col=json.loads(resp.text)
    if(col["status"]=="OK"):        
        rgb=base64.b64decode(col["result"])
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
    else:
        print("No settings found, light off by default.")
        
    
    print("The light is currently in the following state:")
    print(color("  ######\n ########\n###########\n###########\n ########\n ########\n  #####\n  #####\n   ##", fore=(r, g, b), back=(0, 0, 0)))
    print("R:%3d, G:%3d, B:%3d"%(r,g,b))
    time.sleep(1)
