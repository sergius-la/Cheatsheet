from datetime import datetime

"""
Декорыторы:
https://www.youtube.com/watch?v=Ss1M32pp5Ew
"""

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

l1 = one
a = l1(10) # [0, 2, 4, 6, 8]

l2 = timeit(one)
b = l2(10) # 0:00:00.000401

