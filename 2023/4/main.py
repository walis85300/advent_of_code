import re


def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def part_one():
    lines = read_file("input.txt")
    total = 0
    for line in lines:
        found = re.findall(r"Card\s+(\d+):\s+([\d\s]+) \| ([\d\s]+)", line)
        card, first, second = found[0]
        card = int(card)
        first = [int(x) for x in first.split()]
        second = [int(x) for x in second.split()]
        a = 0
        for i in first:
            if i in second:
                a += 1
        if a == 0:
            continue
        total += 2 ** (a - 1)
    print(total)


def main():
    part_one()


if __name__ == "__main__":
    main()
