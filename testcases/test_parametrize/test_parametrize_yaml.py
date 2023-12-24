import pytest
import requests
import yaml


def get_data():
    f = open("../../config/data.yaml", encoding="utf-8")
    data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="function", autouse=True)
def func():
    print("前置步骤：数据初始化。。。")


@pytest.mark.parametrize("shouji,appkey", get_data()['mobile_params'])
def test_mobile(shouji,appkey):
    params={"shouji":shouji,"appkey":appkey}
    print(params)
    r = requests.get('https://api.binstd.com/shouji/quer',params=params)
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']['shouji'] == "13456755448"
    assert result['result']['province'] == "浙江"
    assert result['result']['city'] == "杭州"
    assert result['result']['company'] == "中国移动"
    assert result['result']['cardtype'] is None
    assert result['result']['areacode'] == "0571"


if __name__ == '__main__':
    pytest.main()
