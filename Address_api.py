from fortiosapi import FortiOSAPI
from pprint import pprint

fgt = FortiOSAPI()

device = {
    'host': 'ip',
    'username': 'xxx',
    'password': 'pwd',
}

fgt.login(**device, verify=False)

address = {
    "name": Address Name,
    "type": Type have to choose,
	"subnet": ip assign,
	"interface": you have to choose
}

# Config address
fgt.set('firewall', 'address', data=address)

# Check
out = fgt.get('firewall', 'address')
print('out for checking',out)
# Print all address names
for address in out['results']:
  print(address['name'])

fgt.logout()