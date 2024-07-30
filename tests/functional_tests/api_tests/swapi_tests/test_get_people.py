import pytest

from core.swapi.asserations.assert_all_people_endpoint import assert_all_people_page_n_endpoint
from core.swapi.helpers import get_starships_of_people, check_starships_are_available


@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1, 2, 'asd'])
def test_get_swapi_user(user_id, swapi_ctrl):

    response = swapi_ctrl.get_people(user_id=user_id)
    starships = get_starships_of_people(response.json())
    check_starships_are_available(starships)


@pytest.mark.swapi
@pytest.mark.parametrize('page', [1, 2, 5])
def test_get_all_swapi_user_page_n(swapi_ctrl, page):

    response = swapi_ctrl.get_all_people(params={'page': page})

    # requests.get(url="https://swapi.dev/api/people/", params={'page': 2, 'limit': 45})  # == GET https://swapi.dev/api/people/?page=2&limit=45

    assert_all_people_page_n_endpoint(response.json(), page)


@pytest.mark.swapi
def test_get_all_swapi_user_page_default(swapi_ctrl):

    response = swapi_ctrl.get_all_people()
    assert_all_people_page_n_endpoint(response.json(), page=1)



