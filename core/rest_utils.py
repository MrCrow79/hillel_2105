import allure
import requests
import json as json_lib
import curlify

import logging

logger = logging.getLogger('execute_request')


class RestUtils:


    @staticmethod
    @allure.step('send request to {method} {url}')
    def execute_request(url: str, method: str, params=None, data=None, json=None, headers=None, status_code=None):
        logger.info(f'request is sending to {method.upper()} {url} with params {params}')
        logger.info(f'with body  data={data}\njson={json}')

        response = getattr(requests, method)(url=url, params=params, json=json, data=data, headers=headers)

        allure.attach(body=json_lib.dumps(dict(response.headers)), name='response headers', attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=curlify.to_curl(response.request), name='curl', attachment_type=allure.attachment_type.TEXT)



        logger.info(f'Status code is {response.status_code}')
        logger.info(f'Data  is {response.text}')

        if status_code:
            assert response.status_code == status_code, \
                f'Status code of {method.upper()} {url} is {response.status_code} but expected {status_code}'

        return response
