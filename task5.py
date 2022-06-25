from math import prod


def count_find_num(primesL, limit):
    res = []
    mn = prod(primesL)
    for i in range(mn, limit+1):
        n = i
        for k in primesL:
            while (n//mn) % k == 0:
                n /= k
        if n == mn:
            res.append(i)
    if not res:
        return res
    else:
        return [len(res), max(res)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
