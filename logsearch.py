from re import findall

with open("C:\Program Files\Suricata\log\eve.json", "r") as file:

  ip_addresses = file.read()

ipmatch = findall(r"\"src_ip\"\:\"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d\"", ip_addresses)

for ip in ipmatch:
  print(ip)
  