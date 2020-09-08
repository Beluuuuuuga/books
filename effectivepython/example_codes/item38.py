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