from web_client import WebClient


def test_get_request(monkeypatch):
    execute_counter = 0  # счётчик вызова mock_get_request
    executed_urls = set()  # извлечённые url

    # Метод извлекает url и считает, сколько раз он был вызван.
    def mock_get_request(*args):
        nonlocal execute_counter, executed_urls
        execute_counter += 1
        executed_urls.add(args[0].url)

    # Замена метода из класса WebClient на mock метод.
    monkeypatch.setattr("web_client.WebClient.get_request", mock_get_request)

    test_url = "https://mc.yandex.ru/watch/545728?wmode=7&page-url=https%3A%2F%2Fwww.gismeteo.ru%2Fweather-sankt-peterburg-4079%2F10-days%2F&page-ref=https%3A%2F%2Fwww.google.com%2F&nohit=1&charset=utf-8&cnt-class=1&uah=chu%0A%22Chromium%22%3Bv%3D%22116%22%2C%22Not)A%3BBrand%22%3Bv%3D%2224%22%2C%22Google%20Chrome%22%3Bv%3D%22116%22%0Acha%0Ax86%0Achb%0A64%0Achf%0A116.0.5845.141%0Achl%0A%22Chromium%22%3Bv%3D%22116.0.5845.141%22%2C%22Not)A%3BBrand%22%3Bv%3D%2224.0.0.0%22%2C%22Google%20Chrome%22%3Bv%3D%22116.0.5845.141%22%0Achm%0A%3F0%0Achp%0AWindows%0Achv%0A10.0.0&browser-info=pv%3A1%3Avf%3A7h8dgiykw9gn99c2hdkydpb%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru-RU%3Av%3A1101%3Acn%3A5%3Adp%3A0%3Als%3A1249333139134%3Ahid%3A967239092%3Az%3A180%3Ai%3A20230905150321%3Aet%3A1693915401%3Ac%3A1%3Arn%3A283026469%3Au%3A1692880487922528981%3Aw%3A423x644%3As%3A1366x768x24%3Ask%3A1%3Awv%3A2%3Aco%3A0%3Acpf%3A1%3Aeu%3A0%3Ans%3A1693915398267%3Aadb%3A2%3Arqnl%3A1%3Ast%3A1693915401%3At%3AGISMETEO%3A%20%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0%20%D0%B2%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5%20%D0%BD%D0%B0%2010%20%D0%B4%D0%BD%D0%B5%D0%B9%2C%20%D0%BF%D1%80%D0%BE%D0%B3%D0%BD%D0%BE%D0%B7%20%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D1%8B%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%20%D0%BD%D0%B0%2010%20%D0%B4%D0%BD%D0%B5%D0%B9%2C%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%20(%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F.&t=mc(p-29-ci-19-h-1)clc(0-0-0)lt(198600)aw(1)ti(2)"
    client = WebClient(test_url)
    # Теперь при вызове метода get_request() будет вызываться mock_get_request().
    # Это нужно для того, чтобы тест не отправлял реальный запрос по url.
    client.get_request()

    # Проверка того, что mock метод был вызван лишь один раз и запрос отправлялся по правильной ссылке.
    assert execute_counter == 1
    assert executed_urls == {test_url}
