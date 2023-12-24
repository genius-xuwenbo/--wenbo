import yaml

f = open("../config/data.yaml", encoding="utf-8")
data = yaml.safe_load(f)
print(data)
print(data['hero'])
print(data['heroes'])
print(data['heroes_name'])
print(data['heroes_name_list'])

def get_data():
    f = open("../config/data.yaml", encoding="utf-8")
    data = yaml.safe_load(f)
    shouji= data['mobile_params'][0]
    #appkey = data['mobile_params'[1]]
    return shouji

if __name__ == '__main__':
    print(get_data())
