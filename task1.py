def bi(n):
    N = abs(n)
    res = 0
    count = 0
    while (N > 0):
        res = (10**count * (N % 2)) + res
        N = N // 2
        count += 1
    if (res >= 0):
        return res
 
    else:
        return ()
 
def foo(n):
    for i in range(1, 65):
        if n < 2**i:
            return i
 
print(bi(123))
print(bi(~123))
num = int(input("Enter a number... "))
c = 0
 
if num < 0:
    num = (abs(num))^(2**foo(abs(num))-1)-1
    c += 1
print(bi(num))
while (num > 1):
    c += num % 2
    num = num // 2
print(c+1)
