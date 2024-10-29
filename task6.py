import pytest

def insert(array, index, elements):
    return array[:index] + elements + array[index+1:]
assert insert([1, 2, 3], 1, [8, 9]) == [1, 8, 9, 3]

def flatten(a, depth = -1):
    count = 0

    while count != depth:
        is_done = True

        for i in range(len(a)):
            if isinstance(a[i], list):
                a = insert(a, i, a[i])
                is_done = False

        if is_done == True:
            break

        count += 1

    return a

assert flatten([1, 2, [4, 5], [6, [7]], 8]) == [1, 2, 4, 5, 6, 7, 8]
assert flatten([1, 2, 3, 4]) == [1, 2, 3, 4]
assert flatten([]) == []
assert flatten([[4]]) == [4]

assert flatten([1, 2, [4, 5], [6, [7]], 8], depth=1) == [1, 2, 4, 5, 6, [7], 8]
assert flatten([[[[1]]]], 2) == [[1]]
