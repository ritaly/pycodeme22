def open_file(filename):
    with open(filename) as file:
        return file.readlines()


namefile = "test.txt"
open_file(namefile)