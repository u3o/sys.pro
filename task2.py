def solution(a, b):
    res = []
    for i in range(min(len(a), len(b))):
        res.append((a[i], b[i]))
    return res

assert solution([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]
assert solution([1, 2], ["a", "b", "c", "d"]) == [(1, "a"), (2, "b")]
assert solution(["a", 2, 3.5], [-3, "c", "c", "c", "c"]) == [("a", -3), (2, "c"), (3.5, "c")]
assert solution([], []) == []
