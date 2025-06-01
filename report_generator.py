from rich.console import Console
from rich.table import Table

console = Console()

def display_nmap_results(results):
    table = Table(title="🔍 Nmap Vulnerability Results")
    table.add_column("Host", style="cyan", no_wrap=True)
    table.add_column("Ports", style="magenta")

    for host, data in results.items():
        ports = [f"{port}/{data['tcp'][port]['state']}" for port in data['tcp']]
        table.add_row(host, ", ".join(ports))

    console.print(table)

def display_shodan_info(info):
    console.print("\n[bold blue]🌐 Shodan Info[/bold blue]")
    for key, value in info.items():
        console.print(f"[yellow]{key}:[/yellow] {value}")
