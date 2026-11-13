import socket
import subprocess
import ipaddress
import platform
from datetime import datetime

def getNetwork():
    hostName= socket.gethostname()
    localIP= socket.gethostbyname(hostName)

    gateway="unknown"

    try:
        if platform.system()=="Windows":
            result=subprocess.check_output(
                "ipconfig", text=True)
        else:
            result=subprocess.check_output(["ip","route","show","default"], 
                                           text=True)
            for line in result.splitlines():
                if"default via" in line:
                    gateway= line.split()[2]
                    break
    except Exception:
        print("Could not determine gateway")

    return localIP, gateway


def getIpClass(ip):
    firstOctet= int(ip.split(".")[0])

    if 1<=firstOctet <=126:
        return "class A"
    elif firstOctet==127:
        return "loopback(reserved)"
    elif 128<=firstOctet<=191:
        return "class B"
    elif 192<=firstOctet<=223:
        return "Class C"
    elif 224<= firstOctet <=239:
        return "Class D(multicast)"
    elif 240<= firstOctet <=255:
        return "class E(experimental)"

    return "unkown"

def discoverHost(localIp):
    print("\nDiscovering active hosts")
    print("-" * 50)


    network=ipaddress.ip_network(
        localIP+"/24",
        strict=False
    )

    activeHosts=[]

    for ip in network.hosts():
        ip=str(ip)

        if ip== localIP:
            activeHosts.append(ip)
            print(f"{ip}: Your device")
            continue

        try:
            if platform.system()=="Windows":
                command=["ping","-n","1","-w","500",ip]
            else:
                command=["ping","-c","1","-W","1",ip]

            result=subprocess.run(
                command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )

        except Exception:
            pass

    return activeHosts


print("=" * 50)
print("       PYTHON HOST DISCOVERY TOOL")
print("=" * 50)

print(f"Scan started: {datetime.now()}")

localIP, gateway= getNetwork()

print("\nNETWORK INFORMATION")
print("-" * 50)
print(f"Local IP Address:{localIP}")
print(f"Gateway IP: {gateway}")
print(f"IP Class:{getIpClass(localIP)}")

activeHosts = discoverHost(localIP)


print("\nSCAN SUMMARY")
print("-" * 50)
print(f"Gateway IP:{gateway}")
print(f"Active Hosts: {len(activeHosts)}")
print(f"Scan completed:{datetime.now()}")
print("=" * 50)
