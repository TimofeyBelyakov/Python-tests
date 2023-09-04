import pytest


path = "tests/test_file_workers/test_file.txt"
count = 1


# Теперь перед каждым тестом будет выполняться эта функция.
# Перед тестированием содержимого файлов, необходимо убедиться, что в нём не будет лишних данных, которые могут помешать
# прохождению теста. Поэтому тестовые файлы нужно очистить.
@pytest.fixture(autouse=True)
def clean_text_file():
    global count
    with open(path, "w"):
        pass
    print(f"\ncount: {count}")
    count += 1
