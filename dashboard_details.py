import requests
import sys
import json

def postURL(url,data_dumps):
	x = requests.post(url, data=data_dumps)
	return x.text
URL1=[['insert_dashboard','/api/v2/monitor/system/status','system'],['insert_dashboard','/api/v2/monitor/license/status','license']]
URL='https://0.0.0.0'
session = requests.session()
res = session.post(URL + '/logincheck', data='username=username&secretkey=password', verify = False)
print res.text
data={}
if res.text.find('error') != -1:
    # Found some error in the response, consider login failed
    print ('LOGIN fail')
    sys.exit()
else:
    print ('LOGIN succeed')
for x in URL1:
	# Retrieve server csrf and update session's headers
	for cookie in session.cookies:
		if cookie.name == 'ccsrftoken':
			csrftoken = cookie.value[1:-1] # token stored as a list
			#print "using crsftoken: %s" % csrftoken
			session.headers.update({'X-CSRFTOKEN': csrftoken})
			
	res = session.get(URL + x[1])
	print res.text
	data[x[2]]=json.loads(res.text)
	#firewall = res.text
	#a = json.loads(firewall)
	data['source']="gt01railtel"
	
finaldata=json.dumps(data)
result = postURL("http://xyz.in/"+x[0],finaldata)
print (result)