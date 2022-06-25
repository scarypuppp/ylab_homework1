from itertools import product


def bananas(s) -> set:
    result = set()
    p = list(product([0, 1], repeat=len(s)))
    for i in range(len(p)):
        curr = list(s)
        for j in range(len(s)):
            if not p[i][j]:
                curr[j] = '-'
        curr = ''.join(curr)
        if curr.replace('-', '') == "banana":
            result.add(curr)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

