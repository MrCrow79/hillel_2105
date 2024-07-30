from core.rest_utils import RestUtils


class SwapiCtrl(RestUtils):

    def __init__(self):
        self.base_url = 'https://swapi.dev/api/'

    def get_people(self, user_id, status_code=200):
        """
        sending get request to  https://swapi.dev/api/people/{user_id}/
        """
        url = f'{self.base_url}people/{user_id}/'
        return self.execute_request(url=url, method='get', status_code=status_code)

    def get_all_people(self, params=None, status_code=200):
        """
        sending get request to  https://swapi.dev/api/people/
        """
        url = f'{self.base_url}people/'
        return self.execute_request(url=url, method='get', params=params, status_code=status_code)

    def get_starships(self, starship_id, status_code=200):
        """
        sending get request to  https://swapi.dev/api/starships/{starship_id}/
        """
        url = f'{self.base_url}starships/{starship_id}/'  # https://swapi.dev/api/ + starships/ + 1 + /
        return self.execute_request(url=url, method='get', status_code=status_code)


