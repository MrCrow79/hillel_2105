import json


list_with_data = (
    {'id': 5, 'name': 'Alex'},
    {'id': 2, 'name': 'Alex2'},
    {'id': 3, 'name': 'Alex3'},
    {'id': 6, 'name': 'Alex4'},
    {'id': 10, 'name': False},
    {'id': 11, 'name': None},
)


file_name = 'json_data.txt'

# with open(file_name, 'w') as f:
#     json.dump(list_with_data, f, indent=4) # write  data


# with open(file_name, 'r') as f:
#     x = f.read()
#     print(x)


with open(file_name, 'r') as f:
    try:
        x = json.load(f)  # read data
        print(x)
    except json.decoder.JSONDecodeError:
        pass


#
# response = """
# [
#     {
#         "id": 5,
#         "name": "Alex"
#     },
#     {
#         "id": 2,
#         "name": "Alex2"
#     },
#     {
#         "id": 3,
#         "name": "Alex3"
#     },
#     {
#         "id": 6,
#         "name": "Alex4"
#     },
#     {
#         "id": 10,
#         "name": false
#     },
#     {
#         "id": 11,
#         "name": null
#     }
# ]"""
#
# response_data = json.loads(response)  # for from-strings
# request_data = json.dumps(response_data)  # to json-strings
#
# import requests
#
#
# response = requests.get('https://lms.ithillel.ua/groups/661fb87151df92075d05c802/lessons/661fb87151df92075d05c81f')
# pass