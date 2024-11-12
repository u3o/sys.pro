def solution(num):
    def foo(n):
        i = 1
        while True:
            if n < 2**i:
                return i
            i += 1

    c = 0
 
    if num < 0:
        num = (abs(num))^(2**foo(abs(num))-1)-1
        c += 1

    while (num > 1):
        c += num % 2
        num = num // 2

    return c+1

#tests
assert solution(-123) == 3
assert solution(10) == 2
