def specialize(func, *args, **kwargs):
    def F(*Fargs, **Fkwargs):
        retArgs = Fargs + args
        for i in Fkwargs:
            kwargs[i] = Fkwargs[i]
        return func(*retArgs, **kwargs)
    return F

def deprecated(f = None, since = None, will_be_removed = None):
    if f is None:
        return specialize(deprecated, since = since, will_be_removed = will_be_removed)
        
    def inner(*args, **kwargs):
        print(f"Warning: function {f.__name__} is deprecated{(" since version " + since) if since != None else ""}. It will be removed in {("version " + will_be_removed) if will_be_removed != None else "future versions"}.")
        return f(*args, **kwargs)
    return inner

#"tests"
@deprecated
def func1(*args):
    print(f"args: {args}")
func1(1,'asdf',3)

@deprecated(since = '1.2', will_be_removed = '3.4')
def func2(*args):
    print(f"args: {args}")
func2(234)

@deprecated(will_be_removed = '2.0')
def func4(*args):
    print(f"args: {args}")
func4(3, 45)

@deprecated(since = '0.3b')
def func3(*args):
    print(f"args: {args}")
func3('dddd', 3, 45)

@deprecated
def func5():
    print("hi")
func5()
