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
    "zero": 0,
}


def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def part_one():
    lines = read_file("part_one.txt")

    number_in_lines = [re.findall(r"\d", line) for line in lines]
    number_in_lines = [f"{number[0]}{number[-1]}" for number in number_in_lines]
    number_in_lines = [int(number) for number in number_in_lines]

    print(sum(number_in_lines))


def get_number(input: str) -> str:
    if input.isnumeric():
        return input
    return str(numbers[input])


def part_two():
    lines = read_file("part_one.txt")

    print(lines)
    keys = list(numbers.keys())
    regex = r"\d|" + "|".join(keys)
    print(regex)

    for line in lines:
        r = re.finditer(regex, line)
        print(r)

        print("----")
        for m in r:
            print(m.group())
        print("----")
        rr = [m.group() for m in r]
        print(rr)
    matches = [re.finditer(regex, line) for line in lines]

    print(matches)
    numbers_in_lines = [
        [match.group() for match in match_list] for match_list in matches
    ]
    print(numbers_in_lines)

    n = [
        f"{get_number(number[0])}{get_number(number[-1])}"
        for number in numbers_in_lines
    ]
    n = [int(number) for number in n]
    print(n)
    # print(len(n))
    # print(sum(n))


if __name__ == "__main__":
    # part_one()
    part_two()

    print("Done!")
