import requests
params={
    "city":"西安",
    "key":"6s6EWyDBaEcKtK5JLqGmp4HPk"
}
r = requests.post(url="https://binstd.apistd.com/weather/query",params=params)
print(r.status_code)
print(r.json())
print(r.text)