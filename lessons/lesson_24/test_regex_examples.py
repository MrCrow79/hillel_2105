import pytest
import re

cities = ['Kyiv', "London" , "washington"]

countries = ['Ukraine', 'grate britain', 'USA']

text = "The {} is the capital of {}"



@pytest.mark.parametrize('data', list(zip(cities, countries))) # [(city, country), (city2, country2), ...]
def test_check_city_country(data):
    city, country = data
    final_text = text.format(city, country)
    # ми знаємо тільки final_text без city, country values

    # assert final_text.startswith('The')
    # assert final_text.split()[1].istitle()
    # assert final_text.split()[-1].istitle()
    print(final_text)
    re_city = "^The\s[A-Z]{1}[a-z]+"
    re_country = "\s[A-Z]+[a-z]*$"
    assert bool(re.findall(re_city, final_text))
    assert bool(re.findall(re_country, final_text))


# номер телефону, пчинаеться з + 1-2 цифри, дужки 3 фири і потім 7 фифр, +38(089)8885522

# "^\+[\d]{1,2}\([\d]{3}\)[\d]{7}$"
