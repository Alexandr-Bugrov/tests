import requests

class YaUploader:
    def __init__(self, Yandextoken: str):
        self.Yandextoken = Yandextoken

    def get_headers(self):
        return {
                'Authorization': f'OAuth {self.Yandextoken}'
                }

    def create_folder(self, file_folderYa: str):
        """Метод создает папку на яндекс диске по ее названию"""
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        folder_params = {'path': file_folderYa,
                         'overwrite': 'True'
                         }
        response = requests.put(folder_url, params=folder_params, headers=headers)
        return response

if __name__ == '__main__':
    yanex = YaUploader('')
    yanex.create_folder('my_folder/')