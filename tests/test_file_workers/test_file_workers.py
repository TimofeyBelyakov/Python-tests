from file_workers import read_from_file


path = "tests/test_file_workers/test_file.txt"


def create_test_data(test_data):
    with open(path, "a") as file:
        file.writelines(test_data)


def test_read_from_file():
    test_data = ["one\n", "two\n", "three\n", "four"]
    create_test_data(test_data)
    assert test_data == read_from_file(path)


def test_read_from_file_2():
    test_data = ["one\n", "two\n", "three\n", "four"]
    create_test_data(test_data)
    assert test_data == read_from_file(path)
