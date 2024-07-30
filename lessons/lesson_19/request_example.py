import requests

for user in [1,2,3,4]:
    response = requests.get(url=f'https://swapi.dev/api/people/{user}/')

    assert response.status_code == 200
    print(response.json())
    print('-'*80)
    print('-'*80)