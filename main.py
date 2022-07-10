import requests
import json
import os



TOKEN = ""
class Test:  
    def get_most_intelligence_superhero(self):
        superheroes_dict = {}
        url = "https://akabab.github.io/superhero-api/api/all.json"
        response_s = requests.get(url)
        response_f = response_s.json()
        for el in response_f:
            if el['name'] == "Hulk":
                superheroes_dict[el['name']] = el
            elif el['name'] == "Captain America":
                superheroes_dict[el['name']] = el
            elif el['name'] == "Thanos":
                superheroes_dict[el['name']] = el
        prom_list = []
        for item in superheroes_dict.items():
            prom_list.append(item[1]['powerstats']['intelligence'])      
        fin_list = sorted(prom_list)
        for intelligence_hero in superheroes_dict.values():
            if intelligence_hero['powerstats']['intelligence'] == fin_list[-1]:
                print(f"Самый умный супергерой это {intelligence_hero['name']}")
        result = superheroes_dict, intelligence_hero['name']
        return result
    
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def OAuth(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def upload(self, filename):
        data_bytes = open(filename, 'rb')
        name = os.path.basename(filename)
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.OAuth()
        params = {"path": name, "overwrite": "true"}
        resp = requests.get(upload_url, headers=headers, params=params).json()
        href = resp.get('href')
        response = requests.put(href, data_bytes)
        if response.status_code == 201:
            print("Загрузка выполнена успешно")

if __name__ == "__main__":
    some_hero = Test()
    some_hero.get_most_intelligence_superhero()
    ya = YaUploader(token=TOKEN)
    ya.upload()