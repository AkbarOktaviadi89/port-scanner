import socket
import argparse
import threading
from queue import Queue
from utils import load_services, save_results

services = load_services()
lock = threading.Lock()
results = []

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                with lock:
                    service = services.get(str(port), "Unknown")
                    results.append({"port": port, "service": service})
                    print(f"[OPEN] Port {port} - {service}")
    except Exception as e:
        pass

def threader(q, target):
    while not q.empty():
        port = q.get()
        scan_port(target, port)
        q.task_done()

def main():
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner")
    parser.add_argument("target", help="Target IP/Domain")
    parser.add_argument("--ports", required=True,
                        help="Port atau range (contoh: 22,80,443 atau 20-25 atau gabungan: 22,80,1000-1010)")
    parser.add_argument("--threads", type=int, default=100, help="Jumlah threads")
    parser.add_argument("--save", action='store_true', help="Simpan hasil ke scan_results.json")

    args = parser.parse_args()

    try:
        port_list = parse_ports(args.ports)
    except Exception as e:
        print("❌ Format port salah. Gunakan format: 22,80,443 atau 20-25 atau 22,80,1000-1010")
        return

    print(f"\n🔍 Memulai scan ke {args.target} pada port: {', '.join(map(str, port_list))}\n")

    q = Queue()
    for port in port_list:
        q.put(port)

    for _ in range(args.threads):
        t = threading.Thread(target=threader, args=(q, args.target))
        t.daemon = True
        t.start()

    q.join()

    if args.save:
        save_results(results)
        print("\n💾 Hasil disimpan di scan_results.json")

if __name__ == "__main__":
    main()
