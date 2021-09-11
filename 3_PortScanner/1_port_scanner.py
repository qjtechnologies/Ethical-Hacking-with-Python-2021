# OUTPUT

# Host: IP address
# Status: Up/down
# Services and Ports:
# <Protocol> || <port> || <service>


# TODO
# Detect the OS of the IP


import nmap3
import json
nmap = nmap3.NmapHostDiscovery()


ip = input("Enter an IP Address(Ex. 192.168.31.1): ")


results = nmap.nmap_portscan_only(ip)

for ip in results.keys():
    if not ip in ['stats','runtime']:
        print("Host: ",ip)
        print("Status: ",results[ip]['state']['state'])
        # Processing Ports
        # print(results[ip]['ports'])
        print("Ports and Services")
        count = 1
        for portDetails in results[ip]['ports']:
            print(f"[{count}]")
            print("  Protocol: ",portDetails['protocol'])
            print("  Port: ",portDetails['portid'])
            print("  Service: ",portDetails['service']['name'])
            count += 1
