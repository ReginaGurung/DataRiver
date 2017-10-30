import requests
import shutil
import os
import sys

print(os.getcwd())
shutil.copy2('/Users/rgurung/Documents/project-x/data/test.json', '/Users/rgurung/Documents/python-requests/test.json')




r = requests.post('http://localhost:2113/web/index.html#/streams/$et-dummy_event', data='test.json')

url = 'http://localhost:2113'
data_json = 'test.json'
headers = {'Content-Type': 'application/json', 'ES-EventType' : '$EVENT', 'ES-EventId ':'$UUID', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=data_json, headers=headers)
