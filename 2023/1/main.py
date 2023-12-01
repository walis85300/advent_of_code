import re

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

joined = {
    "oneight": "oneeight",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "sevenine": "sevennine",
    "eightwo": "eighttwo",
    "eighthree": "eightthree",
    "nineight": "nineeight",
    "twone": "twoone",
}


def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def get_number(input: str) -> str:
    if input.isnumeric():
        return input
    return str(numbers[input])


def part_one():
    lines = read_file("part_one.txt")

    number_in_lines = [re.findall(r"\d", line) for line in lines]
    number_in_lines = [f"{number[0]}{number[-1]}" for number in number_in_lines]
    number_in_lines = [int(number) for number in number_in_lines]

    print(sum(number_in_lines))


def part_two():
    lines = read_file("part_one.txt")

    for joined_key, joined_value in joined.items():
        lines = [line.replace(joined_key, joined_value) for line in lines]

    print("aaa", lines)
    keys = list(numbers.keys())
    regex = r"\d|" + "|".join(keys)
    print(regex)

    numbers_in_lines = [re.findall(regex, line) for line in lines]

    n = [
        f"{get_number(number[0])}{get_number(number[-1])}"
        for number in numbers_in_lines
    ]
    n = [int(number) for number in n]
    print(sum(n))


if __name__ == "__main__":
    part_one()
    part_two()

    print("Done!")
