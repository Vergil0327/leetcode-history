# Intuition

確認有無合法解很直覺, 每個位置都嘗試放置每個字母, 最後看有沒有合法cost即可
定義: dfs(i, prev, consecutive): the minimum operation to have good caption considering first `i` characters and previous character is `prev` repeated `consecutive` times.

為了幫助cache, 我們`consecutive >= 3`後其實都是一樣意思, 所以最多只取到3

```py
def minCostGoodCaption(self, caption: str) -> str:
    n = len(caption)
    OFFSET = ord("a")

    dp = [[[-1]*4 for _ in range(27)] for _ in range(n+1)]
    def dfs(i, prev, consecutive):
        if i >= n:
            return 0 if consecutive >= 3 else inf
        if dp[i][prev][consecutive] != -1: return dp[i][prev][consecutive]
        
        cur = ord(caption[i])-OFFSET
        res = inf

        if prev == 26 or consecutive >= 3:
            for j in range(26):
                cost = dfs(i+1, j, 1)
                res = min(res, cost + abs(cur-j))

        if prev != 26:
            cost = dfs(i+1, prev, min(3, consecutive+1)) + abs(cur - prev)
            res = min(res, cost)

        dp[i][prev][consecutive] = res
        return dp[i][prev][consecutive]
```

最難就是該如何利用我們前面拿到的db table, 回頭建構出合法的**lexicographically smallest good caption**
但其實需要做的, 就是在同樣一次recursion, 然後計算cost挑選出lexicographically smallest character

然後這邊我們把兩個part順序調換一下, 因為我們`ch`要挑**lexicographically smallest**
第一部分先:

```py
# turn caption[i] into prev and append
if prev != 26:
    cst = dfs(i+1, prev, min(3, consecutive+1))
    if cst < inf and cst + abs(cur - prev) < cost:
        cost = cst + abs(cur - prev)
        ch = prev
```

第二部分再:

```py
# start new groups with j character
if prev == 26 or consecutive >= 3:
    for j in range(26):
        cst = dfs(i+1, j, 1)
        if cst < inf:
            if cst + abs(cur - j) < cost:
                cost = cst + abs(cur - j)
                ch = j
            elif cst + abs(cur - j) == cost:
                ch = min(ch, j)
```

這是因為, 看這個example: caption = "antwfdps", expected = "nnnnnppp"
如果我們一二部分對調會得到: "nnnppppp"

我們就看中間關鍵的`wf` ("ant{wf}dps"), `wf`不管換成`nn`或是`pp`, 所需cost加總都是17
那根據字典序, 我們要的是"nn"而不是"pp", 而這部分會透過`ch = min(ch, j)`選出相同cost下字典序最小的的決策
所以建構過程為:

```py
self.res = [""] * n
def build(i, prev, consecutive):
    if i >= n: return

    cur = ord(caption[i])-OFFSET
    ch, cost = 26, inf

    # turn caption[i] into prev and append
    if prev != 26:
        cst = dfs(i+1, prev, min(3, consecutive+1))
        if cst < inf and cst + abs(cur - prev) < cost:
            cost = cst + abs(cur - prev)
            ch = prev

    # start new groups with j character
    if prev == 26 or consecutive >= 3:
        for j in range(26):
            cst = dfs(i+1, j, 1)
            if cst < inf:
                if cst + abs(cur - j) < cost:
                    cost = cst + abs(cur - j)
                    ch = j
                elif cst + abs(cur - j) == cost:
                    ch = min(ch, j)

    self.res[i] = chr(ch + OFFSET)
    if ch == prev:
        build(i+1, prev, min(3, consecutive+1))
    else:
        build(i+1, ch, 1)
```

整個主幹為:

```py
cost = dfs(0, 26, 0)
if cost == inf: return ""

self.res = [""] * n
build(0, 26, 0)
return "".join(self.res)
```

雖然整體思緒流暢, C++會跑過, 但最終python跑起來還是會TLE.
優化後改成bottom-up形式依舊TLE
建議理解思緒即可

如果要通過test, 可參考[[Python3] dp by @Ye Gao](https://leetcode.com/problems/minimum-cost-good-caption/solutions/6358081/python3-dp/?slug=minimum-cost-good-caption&region=global_v2)