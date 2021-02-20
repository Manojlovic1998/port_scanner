import socket

from IPy import IP


ipAdress = input('[+] Enter Target To Scan: ')
port = 80

try:
    """Defines socket descriptor."""
    sock = socket.socket()
    """Connect to target machine."""
    sock.connect((ipAdress, port))
    print("[+] Port 80 is open!")
except:
    print("[-] Port 80 is closed.")