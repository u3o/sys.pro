def solution(a, b):
    res = []
    for i in range(min(len(a), len(b))):
        res.append((a[i], b[i]))
    return res

a = [1, 2, 3]
b = ["a", "b"]

print(solution(a, b))
