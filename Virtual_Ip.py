from fortiosapi import FortiOSAPI
from pprint import pprint

fgt = FortiOSAPI()

device = {
    'host': 'ip',
    'username': 'xxxx',
    'password': 'pwd',
}

fgt.login(**device, verify=False)

vip = {
    "name": "Test Virtual IP",
	"extip": "0.0.0.0",
	"extintf": "any",
	"type": "static-nat",
	"mappedip": [{"q_origin_key": "0.0.0.0",
				  "range":"0.0.0.0"}]
}
print(vip)
sett = fgt.set('firewall', 'vip', data=vip)
print(set.__dict__)
out = fgt.get('firewall', 'vip')

pprint(sett)
fgt.logout()