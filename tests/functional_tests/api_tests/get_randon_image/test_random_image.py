import requests


def test_custom_image():

    url = "https://www.gstatic.com/images/icons/material/system/2x/feedback_grey600_24dp.png"

    response = requests.get(url=url)

    with open(r'D:\hillel\pythonProject\hillel_2105\tests\functional_tests\api_tests\get_randon_image\my_feedback_grey600_24dp.png', 'wb') as f:

        f.write(response.content)

    with open(
        r'D:\hillel\pythonProject\hillel_2105\tests\functional_tests\api_tests\get_randon_image\my_feedback_grey600_24dp.png',
        'rb') as f:

        data = {'file_name': f}


    requests.post(url=url, files=data)

