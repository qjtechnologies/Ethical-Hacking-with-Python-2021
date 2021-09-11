import nmap3
import json
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.31.0/24")
print(json.dumps(results))