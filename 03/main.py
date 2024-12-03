import re


def read_file():
    with open("input.txt", encoding='UTF8') as f:
        return f.read()

file = read_file()

regex = "(mul\((\d+),(\d+)\)|do\(\)|don't)"

matches = re.findall(regex, file)

res = 0
enabled = True
for match in matches:
    print(match)
    if match[0] == "do()":
        enabled = True
    elif match[0] == "don't":
        enabled = False
    elif enabled:
        res += int(match[1]) * int(match[2])

print(res)


