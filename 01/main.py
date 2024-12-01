def read_file():
    with open("input.txt", encoding='UTF8') as f:
        return f.read().splitlines()

file = read_file()

first, second = [], []
for line in file:
    a, b = map(int, line.split("   "))
    first.append(a)
    second.append(b)

first_sorted, second_sorted = sorted(first), sorted(second)
print(first_sorted)
print(second_sorted)

res = [abs(a - b) for a, b in zip(first_sorted, second_sorted)]
print(sum(res))

res = [num * second_sorted.count(num) for num in first_sorted]
print(res)
print(sum(res))