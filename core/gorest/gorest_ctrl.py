import os

from core.rest_utils import RestUtils

from utils.setting_utils import settings


class GorestCtrl(RestUtils):
    __auth_token = None

    def __init__(self):
        self.base_url = settings[os.environ['WORKING_ENV']]['GOREST_BASE_URL']  # os.environ['WORKING_ENV'] = dev
        self.auth_token = 'e16964bc5ecb95e03372e807484575d60cc84bfbf17ee43cb7b116e6735ca458'

    def get_user(self, user_id, status_code=200):
        """
        sending get request to  https://gorest.co.in/public/v2/users/{user_id}
        """
        url = f'{self.base_url}users/{user_id}'
        return self.execute_request(url=url, method='get',
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)

    def create_users(self, json: dict, status_code=201):
        """
        sending post request to  https://gorest.co.in/public/v2/users/
        """
        url = f'{self.base_url}users/'
        return self.execute_request(url=url, method='post', json=json,
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)

    def delete_user(self, user_id: str, status_code=204):
        """
        sending delete request to  https://gorest.co.in/public/v2/users/{user_id}
        """
        url = f'{self.base_url}users/{user_id}'
        return self.execute_request(url=url, method='delete',
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)

    def create_post(self, user_id: str, post_body=None, status_code=201):
        """
        sending post request to  https://gorest.co.in/public/v2/users/{user_id}/posts
        """
        url = f'{self.base_url}users/{user_id}/posts'
        return self.execute_request(url=url, method='post', json=post_body,
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)

    def get_user_posts(self, user_id: str, status_code=200):
        """
        sending get request to  https://gorest.co.in/public/v2/users/{user_id}/posts
        """
        url = f'{self.base_url}users/{user_id}/posts'
        return self.execute_request(url=url, method='get',
                                    headers={'Authorization': f'Bearer {self.auth_token}'}, status_code=status_code)
