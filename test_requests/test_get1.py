import requests
r=requests.get("https://api.github.com/events")
print(r.status_code)
print(r.json()) #接口的json
print(r.text)#  接口返回的文本