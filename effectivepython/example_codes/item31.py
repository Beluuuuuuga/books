# Example 01
print('\nExample 01')
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 *value / total
        result.append(percent)
    return result


# Example 02
print('\nExample 02')
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


# Example 03
print('\nExample 03')
path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

# Example 04
print('\nExample 04')
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)
    

# Example 05
print('\nExample 05')
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))


# Example 06
print('\nExample 06')
def normalize_copy(numbers):
    numbers = list(numbers) # イテレータをコピー
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 *value / total
        result.append(percent)
    return result


# Example 07
print('\nExample 07')
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0


# Example 08
print('\nExample 08')
def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


# Example 9
print('\nExample 09')
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0
