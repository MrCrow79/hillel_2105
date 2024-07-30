import requests

import logging

logger = logging.getLogger('execute_request')


class RestUtils:
    @staticmethod
    def execute_request(url: str, method: str, params=None, data=None, json=None, headers=None, status_code=None):
        # getattr(requests, method) == requests.get ,    (url=url, params=params, data=data, headers=headers)
        response = getattr(requests, method)(url=url, params=params, json=json, data=data, headers=headers)
        # requests.get(url="https://swapi.dev/api/people/", params={'page': 2, 'limit': 45})  # == GET https://swapi.dev/api/people/?page=2&limit=45


        logger.info(f'request was send to {response.request.url}')
        logger.info(f'Status code is {response.status_code}')


        # if method == 'get':
        #     requests.get(url=url, params=params, data=data, headers=headers)
        #
        # if method == 'post':
        #     requests.post(url=url, params=params, data=data, headers=headers)
        #
        # if method == 'put':
        #     requests.put(url=url, params=params, data=data, headers=headers)
        # ....

        if status_code:
            assert response.status_code == status_code, \
                f'Status code of {method.upper()} {url} is {response.status_code} but expected {status_code}'

        return response
