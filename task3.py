import pytest

a = ""

def solution(a):
    arr = a.split(" | ")

    for i in range(len(arr)):
        arr[i] = arr[i].split()
    
    return arr

arr = solution(a)

#tests
assert solution("1 2 | 3 4") == [['1', '2',], ['3', '4']]
assert solution("1 2 3 | 4 5 | 6") == [['1', '2', '3'], ['4', '5'], ['6']]
assert solution("") == [[]]
assert solution(" | ") == [[], []]
