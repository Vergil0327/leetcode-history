# Intuition

brute force
```py
def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
    mod = 10 **9 + 7

    packages.sort()
    for box in boxes:
        box.sort()
    impossible = set()

    arr = []
    for i, box in enumerate(boxes):
        if box[-1] >= packages[-1]: # have valid box
            arr.append(box)
    if not arr: return -1

    n, m = len(packages), len(arr)
    dp = [0] * m
    for i in range(n-1, -1, -1):
        for j in range(m):
            idx = bisect.bisect_left(arr[j], packages[i])
            dp[j] = (dp[j] + arr[j][idx] - packages[i])%mod

    return min(dp)
```

從packages出發找box行不通, 會TLE
這時反過來想

我們packages[i]一定是找一個恰好>=他的box來裝
所以我們可以由小到大遍歷每個box_size, 就能用bisect_right找出當前box_size所能涵蓋的packages, 直到涵蓋整個packages[0:n]

所以如果`r = bisect.bisect_right(packages, size)`, 那麼當前box_size就會使用(r-l)個, 所以:

```py
total_used_box_size += box_size * (r-l)
```

等到我們遍歷完, 知道總共使用的所以total_used_box_size後, 再扣掉sum(packages)就是我們的waste size

base case: 遍歷過程中, 如果sorted(box)[-1] < sorted(packages)[-1], 代表該組箱子不適用

```py
minUsedBoxSize = inf
for i, box in enumerate(boxes):
    box.sort()
    if box[-1] < packages[-1]: continue # doesn't fit

    l = boxSize = 0
    for size in box:
        r = bisect.bisect_right(packages, size)
        boxSize = (boxSize + size * (r-l))
        l = r
    minUsedBoxSize = min(minUsedBoxSize, boxSize)

return -1 if minUsedBoxSize == inf else minUsedBoxSize - sum(packages)
```
