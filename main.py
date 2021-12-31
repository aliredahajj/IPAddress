from functions import *
IP = input("Enter the IP:\n")
subs =  int(input("Enter how many subnets:\n"))
IP_s = IP.split(".")


print("IP Address: ", IP)
print("Class: ", class_checker(IP_s[0]))
print("Network Portion: ", network_and_host_checker(IP_s)[0], " | ", "Host Portion: ", network_and_host_checker(IP_s)[1])
print("Network IP: ", network_IP(IP_s))
print("Broadcast IP: ", broadcast_IP(IP_s))
print("Number Of Networks: ", numberOfNetworks(IP_s))
print("Number Of Hosts: ", numberOfHosts(IP_s))
print("Subnet Mask: ", f"{subnet_mask(IP_s, subs)[0]}.{subnet_mask(IP_s, subs)[1]}.{subnet_mask(IP_s, subs)[2]}.{subnet_mask(IP_s, subs)[3]}")
print("Subnet IP: ", subnet_ip(IP_s, subs))