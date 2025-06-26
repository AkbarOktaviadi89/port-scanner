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

    open_ports = sorted([res for res in results if res['status'] == 'open'], key=lambda x: x['port'])

    if open_ports:
        console.rule("[bold green] Open Ports Summary [/]")
        for res in open_ports:
            port = res['port']
            banner = res['banner'].strip() or "No banner"
            console.print(f"[green]Port {port:>5} is OPEN[/] ➜ [cyan]{banner}[/]")
    else:
        console.print("\n[bold red]No open ports found.[/]")

    
    open_ports = [res['port'] for res in results if res['status'] == 'open']
    if open_ports:
        console.print("\n[bold green]Daftar Port Terbuka:[/]")
        console.print(", ".join(map(str, open_ports)))
    else:
        console.print("\n[bold red]Tidak ada port yang terbuka.[/]")
    
    if Prompt.ask("\n[bold yellow]Simpan hasil ke file? (y/n)[/]") == 'y':
        save_results(host, results)
        console.print("[bold green]Hasil disimpan![/]")

if __name__ == "__main__":
    main()
