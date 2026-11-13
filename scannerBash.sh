#!/bin/bash


if ! command -v nmap &> /dev/null; then
    echo "Error: nmap is not installed. Install it using 'sudo apt install nmap'."
    exit 1
fi

targetIP="$1"
NSEscript="$2"

if [ -z "$targetIP" ]; then
    read -p "Enter Target IP (or hostname): " targetIP
fi

if [ -z "$NSEscript" ]; then
    read -p "Enter NSE Script name: " NSEscript
fi


if [ -z "$targetIP" ] || [ -z "$NSEscript" ]; then
    echo "Error: Both Target IP and NSE script name are required."
    echo "Usage: $0 <targetIP> <NSEscript>"
    exit 1
fi

 
echo "Running Nmap scan......."
echo "Target : $targetIP"
echo "Script : $NSEscript"
 
nmap --script="$NSEscript" "$targetIP"