import allure
import pytest


@allure.epic('EEEpic mark')
@allure.feature('Piu-piu feature')
@allure.title('PTitle, hust a title')
@pytest.mark.parametrize('num', [1,2,3])
def test_123(num):
    print(num)