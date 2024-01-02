def ip(x, y):
    return not (x or y) or (x and y)

# Test cases
test_cases = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1)
]

for x, y in test_cases:
    result = ip(x, y)
    print(f"ip({x}, {y}) = {int(result)}")