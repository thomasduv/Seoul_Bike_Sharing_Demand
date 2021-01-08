import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = [[4,-3.4,75,0.0,1982,-7.2,0.0,0.0,0.4,2017,6,12,1,0,1,1],
[20,26.9,49,2.1,2000,15.2,0.0,0.0,0.0,2018,1,9,4,0,1,2],
[13,10.8,44,2.0,935,-0.9,1.01,0.0,0.0,2018,11,19,4,0,1,1],
[23,18.8,73,0.8,291,13.8,0.0,0.0,0.0,2018,5,14,2,0,1,1]]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)