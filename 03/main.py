import re



def read_file():
    with open("input.txt", encoding='UTF8') as f:
        return f.read()

corrupted_memory = read_file()



pattern = r"mul\((\d+),(\d+)\)"

# Find all matches in the corrupted memory
matches = re.findall(pattern, corrupted_memory)


res = 0
for match in matches:
    a, b = map(int, match)
    res += a * b

print(res)