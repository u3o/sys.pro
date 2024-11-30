def coroutine(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        next(ret)
        
        return ret

    return inner


@coroutine
def storage():
    values = []
    while True:
        val = yield
        print(values)
        values.append(val)

g = storage()

g.send(8)
g.send(6)
g.send(9)
g.send(22)
g.send(None)
