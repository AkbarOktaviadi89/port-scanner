import json
from datetime import datetime

def save_results(host, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_filename = f"scan_{host}_{timestamp}.txt"
    json_filename = f"scan_{host}_{timestamp}.json"

    open_ports = [res for res in results if res['status'] == 'open']

    with open(txt_filename, 'w') as f:
        f.write(f"Scan Results for {host} (Only Open Ports)\n")
        f.write(f"Generated at: {timestamp}\n\n")
        if not open_ports:
            f.write("No open ports found.\n")
        else:
            for res in open_ports:
                banner = res['banner'].strip() or "No banner"
                f.write(f"Port {res['port']:>5} is OPEN -> {banner}\n")

    with open(json_filename, 'w') as f:
        json.dump(open_ports, f, indent=2)

    print(f"\n[+] Results saved to:\n- {txt_filename}\n- {json_filename}")
