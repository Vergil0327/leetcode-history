# Intuition

palindrome -> can split into many pairs
since we can rearrange, we can just check how many pairs exist within s[lefti:righti]

first, we can create a prefix sum of characters:
```py
# O(26n)
counters = [defaultdict(int) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(26):
        ch = chr(ord("a")+j)
        counters[i][ch] = counters[i-1][ch]
    counters[i][s[i-1]] += 1
```

then, for each queries[i], we can use O(26) to get how many characters within s[lefti:righti]
```py
remaining = 0
counter = Counter()
for i in range(26):
    ch = chr(ord("a")+i)
    counter[ch] = counters[r+1][ch]-counters[l][ch]

    # for each character, we record its modulo of 2
    remaining += counter[ch]%2
```

then, let's say remaining is 4, it means we have 4 different characters can't rearrange as pair.
as for 4 different characters, we only need 2 operations to make these 4 to form 2 pairs

thus, each queries[i]'s answer is remaining//2 <= k

# Other Solution - bitmask

因為最多就26個字母, 所以用32位bitmask綽綽有餘
再來他僅記錄parity

```py
dp = [0]*(len(s)+1) # store s[:i] for i from 0 to s+1
# dp[i]: # of singles situation of s[:i]
for i in range(1, len(s)+1):
    # dp[digit] toggles on for odd amount toggles off for even amount
    # if already odd, xor makes it even, if even, xor makes it odd
    dp[i] = dp[i-1]^(1<<ints[i-1])
```

再來就是在每個queries[i]下, 確認每個區間內有哪些字母是奇數
```py
interval = dp[r+1]^dp[l]
while interval:
    singles += interval & 1
    interval >>= 1
```

```py
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        ints = [ord(c)-97 for c in s]
        # build dp for all up to i substrings
        dp = [0]*(len(s)+1) # store s[:i] for i from 0 to s+1
        # dp[i]: #  of singles situation of s[:i]
        for i in range(1, len(s)+1):
            # dp[digit] toggles on for odd amount toggles off for even amount
            # if already odd, xor makes it even, if even, xor makes it odd
            dp[i] = dp[i-1]^(1<<ints[i-1])
        for l, r, k in queries:
            # get # of all singled out elements by counting 1 bits
            singles = 0
            interval = dp[r+1]^dp[l]
            while interval:
                singles += interval & 1
                interval >>= 1
            ans.append(singles//2<=k)
        return ans
```