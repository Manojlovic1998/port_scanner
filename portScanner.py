import socket

from IPy import IP

def scan_port(ipAdress, port):
    try:
        # Defines socket descriptor.
        sock = socket.socket()
        # timeout
        sock.settimeout(0.5)
        # Connect to target machine.
        sock.connect((ipAdress, port))
        print(f"[+] Port {str(port)} is open!")
    except:
        print(f"[-] Port {str(port)} is closed.")

ipAdress = input('[+] Enter Target To Scan: ')

for port in range(75, 85):
    scan_port(ipAdress, port)