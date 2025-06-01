import argparse
from nmap_scanner import scan_target
from shodan_lookup import shodan_lookup
from report_generator import display_nmap_results, display_shodan_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a host for vulnerabilities")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--shodan", help="Shodan API key", required=False)
    args = parser.parse_args()

    nmap_results = scan_target(args.target)
    display_nmap_results(nmap_results)

    if args.shodan:
        shodan_results = shodan_lookup(args.target, args.shodan)
        display_shodan_info(shodan_results)
