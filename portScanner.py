import socket

from IPy import IP


def check_ip(address):
    """Checks the ipAddress value, if it is
    ip address of the target then it returns it.
    If the value is domain name then it converts it
    to the ip address.

    Args:
        address (string): It can be an Ip address or it
        can be a domain name.

    Returns:
        [string]: Returns ip address of targeted machine.
    """
    try:
        IP(address)
        return address
    except ValueError:
        return socket.gethostbyname(address)


def scan_port(ipAdress, port):
    """Makes connection with target machine using ipAdress
    and then it scans for open ports.
    
    Args:
        ipAdress (string): Ip address of the machine you are targeting. 
        port (integer): Number of port to be checked.
    """
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
convert_address = check_ip(ipAdress)

for port in range(75, 85):
    scan_port(ipAdress, port)