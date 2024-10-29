a = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}

res = {}

for i in a:
    vals = []

    for j in a:
        if a[i] == a[j]:
            vals.append(j)

    if len(vals) == 1:
        res[a[i]] = vals[0]
    elif len(vals) > 1:
        res[a[i]] = tuple(i for i in vals)

print(res)
