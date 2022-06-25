from math import floor, log


def zeros(n):
    res = 0
    if n == 0:
        return 0
    kmax = floor(log(n, 5))
    for k in range(kmax):
        res += n / 5**(k+1)

    return floor(res)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
