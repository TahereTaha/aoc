
def is_x_pattern_present_in_number(number : str, pattern_size : int) -> int:
    if (len(number) % pattern_size != 0):
        return 0
    sections_count = int(len(number) / pattern_size)
    pattern = number[:pattern_size]
    for x in range(1, sections_count):
        if (number[x * pattern_size:(x + 1) * pattern_size] != pattern):
            return 0
    return 1

def is_pattern_present_in_number(number : str) -> int:
    pattern_sizes : list[int] = []
    for pattern_size in range(1, len(number)):
        if (len(number) % pattern_size == 0):
            pattern_sizes.append(pattern_size)
    for pattern_size in pattern_sizes:
        if (is_x_pattern_present_in_number(number, pattern_size)):
            return 1
    return 0

def get_incorrect_ids_in_range(Range : list[int]) -> list[int]:
    errors : list[int] = []
    for number in range(Range[0], Range[1] + 1):
        if (is_pattern_present_in_number(str(number))):
            errors.append(number)
    return errors


f = open("input", "r")

text : str                  = f.read()[:-1]

ranges : list[str]          = text.split(",")
ranges : list[list[int]]    = [[int(y) for y in x.split("-")] for x in ranges]

errors : list[int]          = []

for x in ranges:
   errors += get_incorrect_ids_in_range(x)

accumulator = 0

for x in errors:
    accumulator += x

#print(errors)
print(accumulator)


