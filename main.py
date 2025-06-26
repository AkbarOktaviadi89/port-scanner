from scanner import PortScanner
from utils import parse_ports, validate_host
from output import save_results
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main():
    console.rule("[bold green]Expert Port Scanner[/]")
    
    host = Prompt.ask("[bold cyan]Masukkan IP atau Hostname[/]")
    if not validate_host(host):
        console.print("[bold red]Host tidak valid![/]")
        return

    port_input = Prompt.ask("[bold cyan]Masukkan port (contoh: 80,443 atau 20-1000)[/]")
    ports = parse_ports(port_input)
    if not ports:
        console.print("[bold red]Format port tidak valid![/]")
        return

    scanner = PortScanner(host, ports)
    results = scanner.scan()

    console.print("\n[bold green]Hasil Pemindaian:[/]")
    for res in results:
        status = "🟢 Open" if res['status'] == 'open' else "🔴 Closed"
        banner = f"[cyan]{res['banner']}[/]" if res['banner'] else "[grey]N/A[/]"
        console.print(f"Port {res['port']:>5}: {status} | {banner}")
    
    if Prompt.ask("\n[bold yellow]Simpan hasil ke file? (y/n)[/]") == 'y':
        save_results(host, results)
        console.print("[bold green]Hasil disimpan![/]")

if __name__ == "__main__":
    main()
