from itertools import combinations


def bananas(s):
    goal = "banana"
    res = set()

    for var in combinations(enumerate(s), len(goal)):
        var_word = ''.join([i[1] for i in var])
        ans = list(s)
        if var_word == goal:
            for vc in enumerate(s):
                if vc not in var:
                    ans[vc[0]] = '-'
            res.add(''.join(ans))
    return res


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

