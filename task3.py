def solution(a):
    arr = a.split(" | ")

    for i in range(len(arr)):
        arr[i] = [float(i) for i in arr[i].split()]
    
    return arr

#tests
assert solution("1.1 2.5 | 3 4.0") == [[1.1, 2.5,], [3.0, 4.0]]
assert solution("1 2 3 | 4 5 | 6") == [[1.0, 2.0, 3.0], [4.0, 5.0], [6.0]]
assert solution("") == [[]]
assert solution(" | ") == [[], []]
