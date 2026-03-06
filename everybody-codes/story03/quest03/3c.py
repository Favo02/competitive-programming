import sys
import re
from collections import defaultdict

child_left = defaultdict(lambda: None)
child_right = defaultdict(lambda: None)
plugs = {}

PLUG = 0
LEFT = 1
RIGHT = 2

def strong(a, b):
    return a == b

def weak(a, b):
    sa, ca = a.split()
    sb, cb = b.split()
    return a != b and (sa == sb or ca == cb)

def construct(root, new, d=0):
    global needed
    # print(" "*d, "attach", new, "to", root, "with constr", needed)
    # if root is None:
    #     return False


    # strong: skip
    if child_left[root] is not None and strong(plugs[root][LEFT], plugs[child_left[root]][PLUG]):
        # print(" "*d, "strong left")
        if construct(child_left[root], new, d+2):
            return True

    # weak: try match
    if child_left[root] is not None and weak(plugs[root][LEFT], plugs[child_left[root]][PLUG]):
        # print(" "*d, "weak left")
        if needed is None and strong(plugs[root][LEFT], plugs[new][PLUG]):
            vagante = child_left[root]
            child_left[root] = new
            needed = new
            if not construct(ROOT, vagante, d+2):
                assert construct(ROOT, vagante, d+2), "secondo giro wrong"
            return True
        if construct(child_left[root], new, d+2):
            return True

    # missing
    if child_left[root] is None:
        # print(" "*d, "no left")
        if needed is None and (weak(plugs[root][LEFT], plugs[new][PLUG]) or strong(plugs[root][LEFT], plugs[new][PLUG])):
            child_left[root] = new
            return True



    # strong: skip
    if child_right[root] is not None and strong(plugs[root][RIGHT], plugs[child_right[root]][PLUG]):
        # print(" "*d, "strong right")
        if construct(child_right[root], new, d+2):
            return True

    # weak: try match
    if child_right[root] is not None and weak(plugs[root][RIGHT], plugs[child_right[root]][PLUG]):
        # print(" "*d, "weak right")
        if needed is None and strong(plugs[root][RIGHT], plugs[new][PLUG]):
            vagante = child_right[root]
            child_right[root] = new
            needed = new
            if not construct(ROOT, vagante, d+2):
                assert construct(ROOT, vagante, d+2), "secondo giro wrong"
            return True
        if construct(child_right[root], new, d+2):
            return True

    # missing
    if child_right[root] is None:
        # print(" "*d, "no right")
        if needed is None and (weak(plugs[root][RIGHT], plugs[new][PLUG]) or strong(plugs[root][RIGHT], plugs[new][PLUG])):
            child_right[root] = new
            return True

    if needed == root:
        needed = None

    return False

ROOT = None
for i, l in enumerate(sys.stdin.read().strip().split("\n")):
    match = re.match(r'id=(\d+), plug=(\w+ \w+), leftSocket=(\w+ \w+), rightSocket=(\w+ \w+), data=(.+)', l)
    id, *rest = match.groups()
    plugs[id] = rest
    # print()
    # print(id, rest)
    global needed
    needed = None

    if i == 0:
        ROOT = id
    else:
        if not construct(ROOT, id):
            assert False, "invalid tree"

    res = []
    def dfs(root):
        if root is None: return
        dfs(child_left[root])
        res.append(int(root))
        dfs(child_right[root])
    dfs(ROOT)
    # print(dict(child_left))
    # print(dict(child_right))
    # print(res)

# print(res)
print(sum((i+1) * r for i, r in enumerate(res)))
