import requests

base_url = 'http://127.0.0.1:8080'

def upload_image(image_path):
    url = f'{base_url}/upload'
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)

    bytes_images = response.content

    with open('file.jpg', 'wb') as f:
        f.write(bytes_images)

upload_image('')
