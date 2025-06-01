import nmap

def scan_target(target):
    scanner = nmap.PortScanner()
    print(f"[+] Scanning {target} with Nmap...")
    scanner.scan(target, arguments='-sV --script vuln')
    
    results = {}
    for host in scanner.all_hosts():
        results[host] = scanner[host]
    return results
