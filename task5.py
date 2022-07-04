from math import prod


def count_find_num(primesL, limit):
    mn = prod(primesL)
    if mn > limit:
        return []
    res = {mn}

    for i in primesL:
        for rn in res:
            rn *= i
            while rn <= limit:
                res.add(rn)
                rn *= i

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
