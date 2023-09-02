# Intuition

since we want the number of k-subsequence with maximum sum, it's intuitively to pick `s[i]` with largest frequency first, then second largest, ... until we pick k s[i] to form a valid k-subsequence.


thus, let's find out s[i] with top k frequency value and group s[i] with same frequency together first.

we use `groups` to store frequency of s[i] in decreasing order.
`groups[i] = [frequency, how many distinct s[i] with same frequency ]`


```py
counter = Counter(s)
maxHeap = []
for ch, cnt in counter.items():
    heapq.heappush(maxHeap, [-cnt, ch])
    
topKGroups = [[0, 0] for _ in range(k)] # [frequency, number of choices]
i = 0
while maxHeap and i < k:
    curMax = maxHeap[0][0]
    topKGroups[i][0] = -maxHeap[0][0]
    while maxHeap and maxHeap[0][0] == curMax:
        topKGroups[i][1] += 1
        heapq.heappop(maxHeap)
    i += 1
```

then we know that `topKGroups[0].frequency > topKGroups[1].frequency > topKGroups[2].frequency > ...`
let's pick s[i] from largest frequency to lowest frequency until we pick k s[i].

if we have `m` choices in current largest frequency:
    - if m <= k: we should pick them all and try to pick extra `k-m` in rest of topKGroups.
      - the frequency of current group is `topKGroups[i][0]` which means we have `topKGroups[i][0]` choices for each s[i] and we can have `topKGroups[i][1]` different `s[i]` to choose
      - thus, `current number of ways *= pow(topKGroups[i][0], topKGroups[i][1])`
    - if m > k: we should choose `k` differenct `s[i]` from total `m` choices, it's `C(m, k)` ways to choose these k different `s[i]`
      - thus, `current number of ways *= C(topKGroups[i][1], k) * pow(topKGroups[i][0], k)`


- if k == 0:
  - it means we have valid k-subsequence, directly return cur
- else:
  - return 0 since we can't form a valid k-subsequence.

# Concise Solution

[lee215](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/solutions/3992969/python-math/)

```py
def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
    count = Counter(s)
    if len(count) < k:
        return 0
    bar = sorted(count.values())[-k]
    res = 1
    mod = 10 ** 9 + 7
    m = 0
    for v in count.values():
        if v > bar:
            k -= 1
            res = res * v % mod
        if v == bar:
            m += 1
    return res * comb(m, k) * pow(bar, k, mod) % mod
```