def assert_all_people_page_n_endpoint(data, page=1):
    assert data['count'] > 0
    assert type(data['results']) is list
    assert len(data['results']) > 0
    if page > 1:
        assert data['previous'] == f"https://swapi.dev/api/people/?page={page - 1}"
    assert data['next'] == f"https://swapi.dev/api/people/?page={page + 1}"
