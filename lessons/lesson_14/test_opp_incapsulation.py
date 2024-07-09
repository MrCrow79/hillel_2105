import pytest

response_alex = {
    'id': 2,
    'Name': 'Alex',
    'sallary': 2000,
    'label': 'junior'
}

response_sofa = {
    'id': 3,
    'Name': 'Sofa',
    'sallary': 3000,
    'label': 'middle'
}


#
# def test_check_response_alex():
#     assert 'id' in response_alex
#     assert 'Name' in response_alex
#     assert 'sallary' in response_alex
#     assert 'label' in response_alex
#
#     assert response_alex['id'] == 2
#     assert response_alex['Name'] == 'Alex'
#
#
# def test_check_response_sofa():
#     assert 'id' in response_sofa
#     assert 'Name' in response_sofa
#     assert 'sallary' in response_sofa
#     assert 'label' in response_sofa
#
#     assert response_sofa['id'] == 3
#     assert response_sofa['Name'] == 'Sofa'


# tests_response.py
@pytest.mark.parametrize('name,id_,data', [
    ('Sofa', 3, response_sofa),
    ('Alex', 2, response_alex),
])
def test_check_response_sofa(name, id_, data):

    ResponseAsserts().assert_response(name, id_, data)  # ResponseAsserts() return instance of ResponseAsserts


# assert_response.py
class ResponseAsserts:

    def __init__(self):
        self.base_fields = ['id', 'Name', 'sallary', 'label']

    def assert_response(self, user_name, user_id, data):
        self.assert_structure(data)  # incapsulations
        self.asset_info_in_data(user_id=user_id, user_name=user_name, data=data)

    def asset_info_in_data(self, user_id, user_name, data):
        assert data['id'] == user_id
        assert data['Name'] == user_name

    def assert_structure(self, data):
        for k in self.base_fields:
            assert k in data
