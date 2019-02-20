# from time import time
mx = 5500

# t = time()
dmloop = []
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))

another_version = list( map(lambda (a, b): divmod(a, b), (range(1, mx), range(a, mx))) )

dmlist = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]

dmgen = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))

"""fibonacci"""
def fibo1(n):
    result = [0]
    next_n = 1
    while next_n <= n:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

def fibo2(n):
    yield 0
    if n == 0:
        return
    a = 0
    b = 1
    while b <= n:
        yield b
        a, b = b, a+b

# list(fibo2(n))

def fibo3(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a+b