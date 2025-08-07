"""
Greedy:

boys的skill由小到大遍歷, 假設skill是`x`, girl's skill優先順序為: x-1 > x > x+1:

因為`x+1`的girl也能跟skill是`x+1`, `x+2`的boy配對
而`x`只能被`x`, `x+1`的boy配對
但`x-1`只能被`x`的boy配對

所以我們優先將`x+1`跟`x`留給更後面的使用, greedily優先找`x-1`的girl
"""

n = int(input())
boys = list(map(int, input().split()))

m = int(input())
girls = list(map(int, input().split()))

from collections import Counter
count = Counter(girls)

boys.sort()
res = 0
for x in boys:
    if count[x-1] > 0:
        count[x-1] -= 1
        res += 1
    elif count[x] > 0:
        count[x] -= 1
        res += 1
    elif count[x+1] > 0:
        count[x+1] -= 1
        res += 1
print(res)

