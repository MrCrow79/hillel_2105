from core.rest_utils import RestUtils


class GorestCtrl(RestUtils):

    __auth_token = None
    def __init__(self):
        self.base_url = 'https://gorest.co.in/public/v2/'
        self.auth_token = 'e16964bc5ecb95e03372e807484575d60cc84bfbf17ee43cb7b116e6735ca458'


    # def get_auth_token(self):
    #     if __class__.auth_token is None:
    #         __class__.auth_token = requests.get(....).json()['token']

    def get_users(self):
        pass

    def create_users(self, json: dict, status_code=201):
        """
        sending get request to  https://gorest.co.in/public/v2/users/
        """
        url = f'{self.base_url}users/'
        return self.execute_request(url=url, method='post', json=json,
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)


