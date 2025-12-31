def abc():
    yield 1   # First value yiels kyeword makes a def/ func to convert it into a generator
    yield 2   # Second value
    yield 3   # Third value

for value in abc():
    print(value)


def count(n):
    c = 1
    while c <= num:
        yield c
        c += 1

for num in count(10):
    print(num)

# gen are meore memory efficient because they generate values on the fly