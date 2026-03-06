import sys
import re
from collections import defaultdict

child_left = defaultdict(lambda: None)
child_right = defaultdict(lambda: None)
plugs = {}

PLUG = 0
LEFT = 1
RIGHT = 2

def mmatch(a, b):
    sa, ca = a.split()
    sb, cb = b.split()
    return sa == sb or ca == cb

def construct(root, new):
    # print("attach", new, "to", root)
    if root is None:
        return False

    if child_left[root] is not None and construct(child_left[root], new):
        return True

    if child_left[root] is None and mmatch(plugs[root][LEFT], plugs[new][PLUG]):
        # print("success")
        child_left[root] = new
        return True

    if child_right[root] is not None and construct(child_right[root], new):
        return True

    if child_right[root] is None and mmatch(plugs[root][RIGHT], plugs[new][PLUG]):
        # print("success")
        child_right[root] = new
        return True

    return False

root = None
for i, l in enumerate(sys.stdin.read().strip().split("\n")):
    match = re.match(r'id=(\d+), plug=(\w+ \w+), leftSocket=(\w+ \w+), rightSocket=(\w+ \w+), data=(.+)', l)
    id, *rest = match.groups()
    plugs[id] = rest
    if i == 0:
        root = id
    else:
        if not construct(root, id):
            assert False, "invalid tree"


res = []
def dfs(root):
    if root is None: return
    dfs(child_left[root])
    res.append(int(root))
    dfs(child_right[root])

# print(plugs)
dfs(root)
# print(res)
print(sum((i+1) * r for i, r in enumerate(res)))
