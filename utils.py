import re
import socket

def parse_ports(port_str):
    try:
        ports = set()
        parts = port_str.split(",")
        for part in parts:
            if '-' in part:
                start, end = map(int, part.split('-'))
                ports.update(range(start, end+1))
            else:
                ports.add(int(part.strip()))
        return sorted(p for p in ports if 0 < p <= 65535)
    except:
        return []

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False
