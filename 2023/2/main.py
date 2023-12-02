import re


def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines


def part_two():
    lines = read_file("input.txt")

    acc = 0

    for line in lines:
        max = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        game, info = line.split(":")
        game = game.strip()
        info = info.strip()

        c = info.split(";")
        for i in c:
            h = i.split(",")
            for j in h:
                j = j.strip()
                number, color = j.split(" ")
                if max[color] < int(number):
                    max[color] = int(number)

        acc = acc + (max["red"] * max["green"] * max["blue"])

    return acc


def part_one():
    lines = read_file("input.txt")
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    acc = 0
    for line in lines:
        game, info = line.split(":")
        game = game.strip()
        info = info.strip()

        game_number = int(re.findall(r"\d+", game)[0])
        c = info.split(";")
        found = False
        for i in c:
            h = i.split(",")
            for j in h:
                j = j.strip()
                number, color = j.split(" ")
                if limits[color] < int(number):
                    found = True
            if found:
                break
        if not found:
            acc += game_number
    return acc


if __name__ == "__main__":
    print(part_one())
    print(part_two())
