def read_file():
    with open("day1.txt", "rb") as f:
        file = f.readlines()

    return list(map(int, file))


def calc_fuel(input):
    return int(input / 3) - 2


def part_two(input):
    total = 0
    fuel = input

    while fuel > 0:
        fuel = calc_fuel(fuel)
        total += fuel if fuel > 0 else 0

    return total


if __name__ == '__main__':
    print(sum(map(calc_fuel, read_file())))
    print(sum(map(part_two, read_file())))
