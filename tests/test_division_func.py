from utils import division
import pytest


# Каждый тестовый модуль должен начинаться со слова test.
# В одном тестовом модуле должен проверяться один набор входных параметров.
def test_division_1():
    assert division(10, 2) == 5


def test_division_2():
    assert division(20, 2) == 10


# Писать отдельный модуль на каждый набор значений неудобно, поэтому можно воспользоваться pytest.
# Декоратор распакует параметры: a, b, expected_result = (10, 5, 2) и т.д.
@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2), (10, -2, -5), (30.5, -2, -15.25)])
def test_division_3(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_exception", [(10, 0, ZeroDivisionError), (10, "2", TypeError)])
def test_division_exceptions(a, b, expected_exception):
    # Ожидаем возникновения исключения. Тест пройдёт успешно.
    with pytest.raises(expected_exception):
        division(a, b)
