import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': 'Netology/test.txt', 'overwrite': 'true'}
        upload_link = requests.get(upload_url, headers=headers, params=params).json()['href']
        with open(path_to_file, 'rb') as data:
            response = requests.put(upload_link, data=data)
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен на Яндекс Диск')


if __name__ == '__main__':
    path_to_file = 'folder/test.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
