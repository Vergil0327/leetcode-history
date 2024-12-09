# Intuition

首先想一下brute force會是怎樣:

我們可以用O(n^2)時間並利用union-find來找出這些connected component
- 對於nums[i] > threshold的數, 其LCM必定超過threshold
- 對於nums[i] <= thresohold的數, 利用union-find找出connected components

```py
def countComponents(self, nums: List[int], threshold: int) -> int:
    n = len(nums)

    nums.sort()
    res = 0
    while nums and nums[-1] > threshold:
        nums.pop()
        res += 1
    
    n = len(nums)

    parent = list(range(n))
    rank = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return

        if rank[px] <= rank[py]:
            parent[px] = py
            rank[py] += rank[px]
        else:
            parent[py] = px
            rank[px] += rank[py]

    for i in range(n):
        for j in range(i-1, -1, -1):
            if lcm(nums[i], nums[j]) <= threshold:
                union(i, j)

    groups = set()
    for i in range(n):
        groups.add(find(i))
    return res + len(groups)
```

但這樣時間上O(n^2)會TLE, 現在重點在於如何優化內部這層循環:

```py
for i in range(n):
    for j in range(i-1, -1, -1):
        if lcm(nums[i], nums[j]) <= threshold:
            union(i, j)
```

對於nums = [2,3,7]來說:
- 2 = 1*2
- 3 = 1*3
- 7 = 1*7

(2,3,7)唯一共通的因數是1, 那麼lcm(2,3) = 2*3, lcm(2,7)=14, lcm(3,7) = 21
這時會發現如果lcm(2,7) <= threshold, 那麼lcm(2*3)一定也小於threshold, 那麼`3`跟`7`都會跟`2` union在一起
因此我們不需要確認(3,7)是否會union在一起

那如果lcm(2,7) > threshold, 那也不用考慮lcm(3,7), 因為只會比lcm(2,7)更大

所以對於`7`來說, 他只要跟每個擁有該`factor`的最小nums[i]比較, 看LCM有沒有小於等於threshold來決定要不要union在一起就好

因此我們額外利用`seen`來存下每個`factor`所見過的第一個nums[i], 這樣之後所有一樣擁有共同`factor`的nums[j]
都可以直接嘗試跟`nums[seen[factor]]` union在一起(如果LCM <= threshold)的話

這樣一來, 原本的O(n^2)就可以降到O(n * sqrt(max(nums)))

```py
# for fixed x and factor d (of x),
# to minimize lcm(x,y) such that y also has a factor d
# it is optimal that y is minimum / minimized
# note: lcm(a,b) = a*b / gcd(a,b)
# so we store the minimum y for each d

seen: {} # {factor: first index from first nums[i] having this factor}
for i in range(n):
    for factor in range(1, int(sqrt(nums[i]))+1):
        if nums[i]%factor == 0:
            x, y = factor, nums[i]//factor

            if x in seen:
                j = seen[x]
                if lcm(nums[i], nums[j]) <= threshold:
                    union(i, j)
            else:
                seen[x] = i

            if y in seen:
                j = seen[y]
                if lcm(nums[i], nums[j]) <= threshold:
                    union(i, j)
            else:
                seen[y] = i
```

time: O(nlogn + n*sqrt(max_num))