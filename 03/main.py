import re


def read_file():
    with open("input.txt", encoding='UTF8') as f:
        return f.read()


def do_dont_mul(memory):
    mul_pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    multiply = True
    total = 0

    for pos in range(len(memory)):

        do_match = re.match(do_pattern, memory[pos:])
        if do_match:
            multiply = True
            pos += do_match.end()
            continue

        dont_match = re.match(dont_pattern, memory[pos:])
        if dont_match:
            multiply = False
            pos += dont_match.end()
            continue

        mul_match = re.match(mul_pattern, memory[pos:])
        if mul_match:
            if multiply:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                total += x * y
            pos += mul_match.end()
            continue

    return total

file = read_file()
print(do_dont_mul(file))

