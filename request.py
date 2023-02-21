# conding=utf-8
import requests
import json

url = 'http://localhost:5005/webhooks/rest/webhook'

lis = ["治疗周期", '哮喘怎么预防', '治疗方式']

# 耳鸣怎么预防
data = {"message": "哮喘怎么预防"}

message = requests.post(url=url, json=data)
print(message.json())
print(message.json()[0])
print(json.loads(message.json()[0]['text']))


