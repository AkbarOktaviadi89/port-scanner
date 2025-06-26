import json
from datetime import datetime

def save_results(host, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_filename = f"scan_{host}_{timestamp}.txt"
    json_filename = f"scan_{host}_{timestamp}.json"

    with open(txt_filename, 'w') as f:
        for res in results:
            f.write(f"{res['port']:>5} - {res['status'].upper()} - {res['banner']}\n")

    with open(json_filename, 'w') as f:
        json.dump(results, f, indent=2)
