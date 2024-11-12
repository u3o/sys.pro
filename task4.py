def solution(a):
    res = {}

    for i in a:

        if list(a.values()).count(a[i]) == 1:
            res[a[i]] = i
        else:
            vals = []
            for j in a:
                if a[i] == a[j]:
                    vals.append(j)
            res[a[i]] = tuple(i for i in vals)

    return res

assert solution({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'} 
assert solution({1: "a", 2: "b", 3: "c", 4: "b", 5: "b", 6: "d", "e": 7, 7: "d"}) == {"a": 1, "b": (2, 4, 5), "c": 3, "d": (6, 7), 7: "e"}

try:
    assert solution({"sdlf": []}) == {[]: "sdlf"}
except TypeError:
    pass
