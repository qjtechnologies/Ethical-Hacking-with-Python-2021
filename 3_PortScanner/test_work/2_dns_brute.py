import nmap3
import json
nmap = nmap3.Nmap()
results = nmap.nmap_dns_brute_script("google.com")
print(json.dumps(results))