import socket
from concurrent.futures import ThreadPoolExecutor
from rich.progress import track

class PortScanner:
    def __init__(self, host, ports, timeout=1, max_threads=100):
        self.host = host
        self.ports = ports
        self.timeout = timeout
        self.max_threads = max_threads

    def scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.host, port))
                if result == 0:
                    try:
                        sock.sendall(b"GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % self.host.encode())
                        banner = sock.recv(1024).decode(errors='ignore').strip()
                    except:
                        banner = ""
                    return {'port': port, 'status': 'open', 'banner': banner}
                else:
                    return {'port': port, 'status': 'closed', 'banner': ''}
        except Exception:
            return {'port': port, 'status': 'error', 'banner': ''}

    def scan(self):
        results = []
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for res in track(executor.map(self.scan_port, self.ports), total=len(self.ports), description="Memindai..."):
                results.append(res)
        return results
