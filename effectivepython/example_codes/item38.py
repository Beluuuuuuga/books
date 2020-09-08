# Example 01
names = ['Scarates', 'Plato', 'Aristotle']
names.sort(key=len)
print(names)


# Example 02
def log_missing():
    print('Key added')
    return 100

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before', dict(result))
for key, amount in increments:
    result[key] += amount
print('After', dict(result))


# Example 03
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0
    
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
print(dict(result))
assert count == 2


# Example 04
class CountMissing:
    def __init__(self):
        self.added = 0
    
    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2