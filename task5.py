def specialize(func, *args, **kwargs):
    def F(*Fargs, **Fkwargs):
        retArgs = Fargs + args
        for i in Fkwargs:
            kwargs[i] = Fkwargs[i]
        return func(*retArgs, **kwargs)

    return F

#tests
def test():
    def sum(x, y):
        return x + y

    five = specialize(sum, x = 2, y = 3)
    plus_one = specialize(sum, y = 1)
    no_defaults = specialize(sum)


    return (five() == 5) and (plus_one(5) == 6) and (no_defaults(5, 4) == 9)
assert test() == True


def test2():
    def sum(x, z, w, y):
        return w+x+y+z

    plus_n = specialize(sum)
    
    return plus_n(1, 2, y=4, w=2) == 9

assert test2() == True
