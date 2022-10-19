from pprint import pprint
import requests

# Задача 1
url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
all_heroes = resp.json()
#pprint(all_heroes)
hero_intelligence = {}
for hero in all_heroes:
    if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
        hero_intelligence[hero['name']] = hero['powerstats']['intelligence']
        max_intelligence = max(hero_intelligence, key=hero_intelligence.get)
print(max_intelligence)


# Задача 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, filename):
        """Метод загружает файл на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        response_json = response.json()
        href = response_json.get('href', '')
        result = requests.put(href, data=open(filename, 'rb'))
        return result


if __name__ == '__main__':
    token = ''
    uploader = YaUploader(token)
    pprint(uploader.upload('Netology/test1710.txt', 'test1710.txt'))


# Задача 3
url = 'https://api.stackexchange.com/2.3/questions?fromdate=1665878400&todate=1665964800&order=desc&sort=activity&tagged=Python&site=stackoverflow'
resp = requests.get(url)
pprint(resp.json())