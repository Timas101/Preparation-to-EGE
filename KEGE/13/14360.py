from ipaddress import *

mask_list = []
for mask in range(17, 31):
    net = ip_network(f'153.202.16.37/{mask}', 0)
    if ip_address('153.202.16.37') not in (net[0], net[-1]) and net.network_address == ip_address('153.202.16.32'):
        print(('1' * mask + '0' * (32 - mask))[16:])
        mask_list.append(('1' * mask + '0' * (32 - mask))[16:])
    
print(mask_list, max(mask_list))


