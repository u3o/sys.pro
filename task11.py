def take(iterable, amount):
    c = 0
    for i in iterable:
        if c < amount:
            yield i 
            c += 1
        else:
            break
#part 1
def cycle(iterable):
    while True:
        for i in iterable:
            yield i
#"tests"
print(list(take(cycle([1,2,3]), 10)))
g = cycle(['a', 'b'])
for i in range(10):
    print(next(g))

#part 2
def chain(*iterables):
    for iterable in iterables:
        yield iterable

#"tests"
g = chain('a', [1, 2], 'b')
print(next(g))
print(next(g))
print(next(g))
