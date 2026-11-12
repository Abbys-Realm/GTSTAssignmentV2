import socket
import  sys
from datetime import datetime

targetHost= input("Enter the target IP/hostname: ")
portRange= input("Enter port range to scan: ")

startPort, endPort= map(int, portRange.split("-"))
print("-" * 50)
print(f"Scanning target: {targetHost}")
print(f"Time start: {str(datetime.now())}")
print("-" * 50)

openPorts=[]

try:
    startTime = datetime.now()

    for port in range(startPort,endPort + 1):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result= s.connect_ex((targetHost, port))
        if result==0:
            print(f"Port {port}: OPEN")
            openPorts.append(port)
        s.close()
except KeyboardInterrupt:
    print("\nExiting the script")
    sys.exit()

except socket.gaierror:
    print("\nHostname couldn't be resolved")
    sys.exit()
except socket.error:
    print("\nCould not conncet to server.")
    sys.exit()


endTime = datetime.now()
duration = endTime - startTime

print("-" * 50)
print("Scanning completed.")
print(f"Total open ports found: {len(openPorts)}")
print(f"Open ports: {openPorts if openPorts else 'None'}")
print(f"Scanning duration: {duration}")
print("-" * 50)