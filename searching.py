import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    file = open(file_path)
    file = json.load(file)
    return file[field]


def main():
    print(read_data("sequential.json","unordered_numbers"))
    pass


if __name__ == '__main__':
    main()