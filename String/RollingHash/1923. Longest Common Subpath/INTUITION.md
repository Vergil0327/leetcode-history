# Intuition

- 要在paths[i]裡找出longest common subarray
- 每個paths[i]是個integer array
- 可以對paths以paths[i].length做排序, res最長可能為paths[0].length

- 如果現在有個valid longest common subarray whose length is n
    - 那代表 n+1 一定不是common subarray
    - 同時也代表n-1一定存在common subarray
    - 由於具有單調性質, 因此我們可以用binary search來找length of longest common subarray
    - search space為: [0, min(paths[i].length)]

因此現在要看如何檢查每個paths[i]存在一個長度為`mid`的common subarray

1. 首先先將paths對len(paths[i])做排序
2. binary search
    - 從paths[0]裡找出所有程度為`mid`的subarray, 並存於hashset裡
        - 如果以tuple方式存, 需要O(mid)時間檢查
        - 如果為TLE/MLE或許要考慮rolling hash
    - 往後檢查看有沒有任意一個subarray存在於paths[1:]內

實際上用tuple來查詢longest common subpath會導致Memory Limit Exceeded(MLE)
```py
def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
    paths.sort(key=lambda x: len(x))
    
    def checkLCS(mid):
        candidates = set()
        for i in range(len(paths[0])-mid+1):
            candidates.add(tuple(paths[0][i:i+mid]))

        for i in range(1, len(paths)):
            nxt = set()
            for j in range(len(paths[i])-mid+1):
                if (tup := tuple(paths[i][j:j+mid])) in candidates:
                    nxt.add(tup)
            if not nxt: return False
            candidates = nxt

        return True

    l, r = 0, len(paths[0])
    while l < r:
        mid = r - (r-l)//2
        if checkLCS(mid):
            l = mid
        else:
            r = mid-1
    return l
```
因此這邊可能要利用rolling hash rather than tuple來檢查longest common subpath

rolling hash:

```py
res = 0
powmod = [pow(n, i, mod) for i in range(len(paths[0]))]
for i in range(mid):
    res += paths[0][i] * powmod[mid-i-1] # powmod[mid-i-1] = pow(n, mid-i-1, mod)
    res %= mod
candidates.add(res)

for i in range(mid, len(paths[0])):
    res -= paths[0][i-mid] * powmod[mid-1] # pow(n, mid-1, mod)
    res *= n
    res += paths[0][i]
    res = (res + mod)%mod
    candidates.add(res)
```

and adjust `mod` to avoid hash collision