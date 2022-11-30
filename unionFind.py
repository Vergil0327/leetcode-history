
# explanation: https://labuladong.github.io/algo/2/22/53/

n = 10
parent = [i for i in range(n)]
rank = [1] * n

# iterative, it won't compress path perfectly
def find(x):
    p = parent[x]
    while p != parent[x]:
        parent[x] = parent[parent[x]]
        p = parent[x]
    return p

# recursion: this is better, it'll compress all the path to O(1)
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)

    if px == py: return False

    if rank[px] >= rank[py]:
        parent[py] = px
        rank[px] += rank[py]
    else:
        parent[px] = py
        rank[py] += rank[px]
    return True

def isConnected(x, y):
    return find(x) == find(y)