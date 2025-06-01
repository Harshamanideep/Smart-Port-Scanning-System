import shodan

def shodan_lookup(ip, api_key):
    api = shodan.Shodan(api_key)
    print(f"[+] Getting Shodan data for {ip}...")
    
    try:
        result = api.host(ip)
        return {
            "IP": result.get("ip_str"),
            "Organization": result.get("org", "N/A"),
            "Operating System": result.get("os", "N/A"),
            "Open Ports": result.get("ports", []),
            "Hostnames": result.get("hostnames", [])
        }
    except shodan.APIError as e:
        return {"Error": str(e)}
