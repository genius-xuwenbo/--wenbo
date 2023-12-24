import requests
'''
json_data={
    "title":"foo",
    "body":"bar",
    "userId":"1"
}

r= requests.post(url="https://jsonplaceholder.typicode.com/posts",json=json_data)
print(r.status_code)
print(r.json())
print(r.text)
'''

datas={
    "text":"hello"

}
r = requests.post(url="https://dict.youdao.com/keyword/key",data=datas)
print(r.status_code)
print(r.json())
#print(r.text)