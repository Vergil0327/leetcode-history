# Intuition

直覺能這樣模擬出過程

```py
def canConvertString(self, s: str, t: str, k: int) -> bool:
    m, n = len(s), len(t)
    if m != n: return False
    moves = Counter(kk%26 for kk in range(1, k+1))
    for i in range(n):
        if s[i] == t[i]: continue

        x = ((ord(t[i]) - ord(s[i]))+26)%26
        
        if moves[x] == 0: return False
        moves[x] -= 1
        
    return True
```

但這樣會TLE, 原因是k最大能到$10^9$級別
所以我們反過來思考, 我們只要看當前s[i]的操作是第幾次更換, 判斷這個操作次序有沒有**小於等於k**即可

```py
moves = [0] * 26
for i in range(n):
    if s[i] == t[i]: continue

    diff = ((ord(t[i]) - ord(s[i]))+26)%26
    moves[diff] += 1
    
    if x + 26 * (moves[diff]-1) > k: return False
```

time: O(n)
space: O(26) = O(1)