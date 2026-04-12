import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    # Читаем файлы (как советуют в задании)
    data1 = json.load(open(args.first_file))
    data2 = json.load(open(args.second_file))

    # Пока просто выводим
    print("File 1:", data1)
    print("File 2:", data2)


if __name__ == "__main__":
    main()