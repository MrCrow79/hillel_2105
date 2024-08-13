import requests

import logging

logger = logging.getLogger('execute_request')


class RestUtils:
    @staticmethod
    def execute_request(url: str, method: str, params=None, data=None, json=None, headers=None, status_code=None):
        response = getattr(requests, method)(url=url, params=params, json=json, data=data, headers=headers)

        logger.info(f'request was send to {method.upper()} {response.request.url}')
        logger.info(f'Status code is {response.status_code}')
        logger.info(f'Data  is {response.text}')


        if status_code:
            assert response.status_code == status_code, \
                f'Status code of {method.upper()} {url} is {response.status_code} but expected {status_code}'

        return response
