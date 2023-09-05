import requests
import json
from datetime import datetime as dt


# Простой веб-клиент.
class WebClient:
    def __init__(self, url):
        self.url = url

    def get_response(self):
        return requests.get(self.url)

    def __get_json_resp(self):
        response = self.get_response()
        return json.loads(response.text)

    # Метод возвращает какие-то настройки.
    def get_settings(self):
        response = self.__get_json_resp()
        return response["settings"]

    # Метод возвращает разницу между текущей и возвращаемой датами в секундах.
    def get_diff_date(self):
        response = self.__get_json_resp()
        resp_date = dt.timestamp(
            dt.strptime(response["settings"]["webvisor"]["date"], "%Y-%m-%d %H:%M:%S")
        )
        current_date = dt.timestamp(dt.now())
        return current_date - resp_date


if __name__ == "__main__":
    url = "https://mc.yandex.ru/watch/545728?wmode=7"

    client = WebClient(url)
    # Получение каких-то настроек.
    print(client.get_settings())
    # Получение разницы между датами в секундах.
    print(client.get_diff_date())
