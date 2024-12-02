def read_file():
    with open("input.txt", encoding='UTF8') as f:
        return [list(map(int, line.split())) for line in f.read().splitlines()]

def is_difference_within_3(a, b):
    return abs(a - b) <= 3 and a != b

def are_all_increasing_by_max_3(report):
    return all(is_difference_within_3(report[i], report[i + 1]) and report[i] < report[i + 1] for i in range(len(report) - 1))

def are_all_decreasing_by_max_3(report):
    return all(is_difference_within_3(report[i], report[i + 1]) and report[i] > report[i + 1] for i in range(len(report) - 1))

def is_valid_with_dampener(report):
    if are_all_increasing_by_max_3(report) or are_all_decreasing_by_max_3(report):
        return True
    return any(are_all_increasing_by_max_3(report[:i] + report[i+1:]) or are_all_decreasing_by_max_3(report[:i] + report[i+1:]) for i in range(len(report)))

file = read_file()
print(file)


## Part 1
print("### Part 1 ###")

res = 0
for report in file:
    if are_all_increasing_by_max_3(report) or are_all_decreasing_by_max_3(report):
        res += 1

print(res)

## Part 2
print("### Part 2 ###")
res = 0
for report in file:
    if is_valid_with_dampener(report):
        res += 1

print(res)