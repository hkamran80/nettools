### How to Use
```py
import nettools
```
### API
`nettools.get_base_ip()`: Returns STR, IP address without suffix (192.168.1)    
`nettools.clean_ip(IP_ADDRESS_LIST)`: Returns STR, IP address from list backwards (see `nettools.nslookup`)    
`nettools.nslookup(IP_ADDRESS)`: Returns DICT, format: `{"ip":IP_ADDRESS, "hostname":HOSTNAME_OF_IP, "owner":OWNER_OF_HOSTNAME/IP}`
