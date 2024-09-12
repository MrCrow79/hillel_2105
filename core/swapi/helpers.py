from core.swapi.swapi_ctrl import SwapiCtrl
import allure


def get_starships_of_people(user_data: dict):
    return user_data['starships']

@allure.step('get infor for next starships: {starships}')
def check_starships_are_available(starships: list):
    for starship in starships:
        SwapiCtrl().execute_request(url=starship, method='get', status_code=200)