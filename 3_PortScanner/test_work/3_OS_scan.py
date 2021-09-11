import nmap3
import json

nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("192.168.31.123")
print(json.dumps(os_results))
