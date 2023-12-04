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
        common = set(first) & set(second)
        a = len(common)
        if a == 0:
            continue
        total += 2 ** (a - 1)
    print(total)


def part_two():
    lines = read_file("input.txt")
    carry = [1] * len(lines)
    for k, line in enumerate(lines):
        found = re.findall(r"Card\s+(\d+):\s+([\d\s]+) \| ([\d\s]+)", line)
        card, first, second = found[0]
        card = int(card)
        first = [int(x) for x in first.split()]
        second = [int(x) for x in second.split()]
        common = set(first) & set(second)
        a = len(common)
        cards = carry[k]
        if a == 0:
            continue

        for j in range(1, a + 1):
            if (j + k) > len(lines):
                break
            carry[j + k] += cards

    print(sum(carry))


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
