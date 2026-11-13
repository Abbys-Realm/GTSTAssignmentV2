# Network Scanning Tools

## Tools

1. **Port scanner without Nmap(portScanner.py)**

- python port scanner that performs port scanning without using the python Nmap module.
- **Consists**: - Accepts a target IP address or hostname - Allows users to specify a port range - Identifies accessible open ports
- **To run**: python portScanner.py

2. **Port scanner using Nmap (portScannerNmap.py)**

- python port scanner that uses the python-nmap library
- **Features**: - Accepts target IP address or hostname - Accepts a port range - Uses Nmap to scan the specified ports - Identify open port and scan results
- **Requirements**: - python3, Nmap, python-nmap
- Install the python library: python -m pip install python-nmap
- **Run**: python portScannerNmap.py 3.**Host Discovery Tools**
- python tool that discovers active devices on a local network.
- **Features**: - Detect the local IP address - Identify the default gateway - Determine IP address class - Discover active hosts on LAN - Display Scan summary

- **Run**: python HostDiscovery.py

4. **Bash Scanner (scannerBash.sh)**

- Bash script that executes nmap NSE scripts against a specified target.
- **Features**: - Checks whether Nmap is installed - Accept the target IP/hostname - Accept NSE script name - Execute the selected Nmap script
- **Requirements**: Linux, Bash, Nmap
- **Run**: - Give permission: chmod +x scannerBash.sh - Run(with/ without argument): ./scannerBash.sh or ./scannerBash.sh 192.168.1.10 http-title
