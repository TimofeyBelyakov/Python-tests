from web_client import WebClient
import responses
from datetime import datetime as dt
import pytest


test_url = "https://mc.yandex.ru/watch/545728?wmode=7"


def test_get_response(monkeypatch):
    global test_url
    execute_counter = 0  # счётчик вызова mock_get_response
    executed_urls = set()  # извлечённые url

    # Метод извлекает url и считает, сколько раз он был вызван.
    def mock_get_response(*args):
        nonlocal execute_counter, executed_urls
        execute_counter += 1
        executed_urls.add(args[0].url)

    # Замена метода из класса WebClient на mock метод.
    monkeypatch.setattr("web_client.WebClient.get_response", mock_get_response)

    client = WebClient(test_url)
    # Теперь при вызове метода get_response() будет вызываться mock_get_response().
    # Это нужно для того, чтобы тест не отправлял реальный запрос по url.
    client.get_response()

    # Проверка того, что mock метод был вызван лишь один раз и запрос отправлялся по правильной ссылке.
    assert execute_counter == 1
    assert executed_urls == {test_url}


@responses.activate
def test_get_diff_time():
    global test_url
    str_date = "2021-04-21 11:07:09"

    # Задаём валидные данные. Указываются как бы возвращаемые данные, они могут быть любыми.
    valid_answer = {"settings": {"webvisor": {"date": str_date}}}
    # Имитация процесса отправки данных.
    responses.add(method=responses.GET, url=test_url, json=valid_answer, status=200)

    client = WebClient(test_url)
    response = client.get_diff_date()

    # Проверка на соответствие между возвращаемой разницей и рассчитанной здесь.
    unix_date = dt.timestamp(dt.strptime(str_date, "%Y-%m-%d %H:%M:%S"))
    current_date = dt.timestamp(dt.now())
    assert response == (current_date - unix_date)


# Негативный тест.
@responses.activate
def test_get_diff_time_with_err():
    broken_url = "https://mc.yandex.ru/watch/545728-?wmode=7"

    valid_answer = {"error": "Not found!"}
    responses.add(method=responses.GET, url=broken_url, json=valid_answer, status=200)

    # Ожидаем KeyError, т.к. в методе get_diff_date() обращаемся у response к полям, которых нет у valid_answer.
    with pytest.raises(KeyError):
        client = WebClient(broken_url)
        client.get_diff_date()
