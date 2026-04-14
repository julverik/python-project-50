import argparse

from gendiff.diff_create import create_diff
from gendiff.formatters.stylish import stylish
from gendiff.parser import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = create_diff(data1, data2)

    if format_name == 'stylish':
        return stylish(diff)
    return stylish(diff)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        default="stylish",
        help="set format of output"
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()