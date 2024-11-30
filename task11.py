import itertools
import numpy

def take(arr, count):
    c = 0
    for i in arr:
        if c < count:
            yield i 
            c += 1
        else:
            break

#wow
def cycle(iterable):
    while True:
        for i in iterable:
            yield i

print(list(take(cycle([1,2,3]), 10)))

g = cycle([1, 2])
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
