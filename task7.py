def deprecated(since = None, will_be_removed = None):
    def actual_deprecated(f):
        def inner(*args, **kwargs):
            nonlocal f

            print(f"Warning: function {f.__name__} is deprecated", end = "")
            print(f" since version {since}.", end = " ") if since != None else print(".", end = " ")
            print(f"It will be removed in", end = " ")
            print(f"version {will_be_removed}.") if will_be_removed != None else print("future versions.")

            ret = f(*args, **kwargs)
            return ret

        return inner
    return actual_deprecated

#"tests"
@deprecated()
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
