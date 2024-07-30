import pytest
import time
import json
from faker import Faker


faker = Faker()
@pytest.mark.gorest
def test_custom_image(gorest_ctrl):
    user_data = {"name": faker.name(), "gender": "male",
                 "email": f"tenali.ramakrishna@{time.time()}.com", "status": "active"}


    # user_data = json.dumps(user_data)
    # response = gorest_ctrl.create_users(data=user_data)
    response = gorest_ctrl.create_users(json=user_data)

    assert response.json().get('id') is not None,  response.json()


