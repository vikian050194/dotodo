import json

from sys import argv


def run():
    source = argv[1]
    with open(source, "r") as fr:
        values = json.load(fr)
        for k in values:
            print(k)


if __name__ == '__main__':
    run()
