# Intuition

利用hashmap紀錄每個階級的票數[# of tier 1 votes, # of tier 2 votes, ...]
然後由大到小排序即可

但要注意的是假如一路同票到最後, 那就需要依照字典序, 因此在rank由大到小排序前, 我們能必須先對team做字典序排列

```py
n = len(votes[0])
rank = defaultdict(lambda: [0] * n)

for v in votes:
    for i in range(n):
        rank[v[i]][i] += 1

teams = sorted(rank.keys()) # sort in alphabetically first
```

```py
return "".join(sorted(teams, key=lambda x:rank[x], reverse=True))
```