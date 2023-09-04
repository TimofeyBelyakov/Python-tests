def read_from_file(path):
    with open(path, "r") as file:
        return file.readlines()


print(read_from_file("prod_file.txt"))
