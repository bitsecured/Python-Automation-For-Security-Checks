# Assign `import_file` to the name of the file 
from re import findall
# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 

#remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open("C:\\Program Files\\Suricata\\log\\eve.json", "r") as file:

  # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

  ip_addresses = file.read()
#regex to find all source ips in log file
ipmatch = findall(r"\"src_ip\"\:\"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d\"", ip_addresses)
# Use `.split()` to convert `ip_addresses` from a string to a list
#ip_addresses = ip_addresses.split("\n")

#to make each log on separate line
for ip in ipmatch:
  print(ip)
  
#print(ip_addresses)
# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`
""""for element in ip_addresses:
  if element in remove_list:
    ip_addresses.remove(element)
print("updated allow list :",ip_addresses)"""
