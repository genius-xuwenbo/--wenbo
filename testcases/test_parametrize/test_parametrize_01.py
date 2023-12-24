import pytest


# @pytest.mark.parametrize("hero", ["VN", "锤石", "辅助"])
# def test_parametrize(hero):
#     print("我喜欢的英雄 " + hero)


@pytest.mark.parametrize("hero,word", [["VN", "让我们来猎杀黑暗中的人们"],
                                       ["纳尔", "想去哪儿，就去哪儿"],
                                       ["酒桶", "来杯朗姆酒"]])
def test_parametrize(hero, word):
    print(f'我喜欢的英雄 {hero} 台词是: {word}')
