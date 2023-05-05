# Intuition

這題很直覺想到的是一個sliding window
一開始的想法是:
我們維護一個window儲存每個字母的個數
我們用O(26)的時間找出最高頻次的字母, 順便在算出總共個數
那這樣就能更新當下的最大字母個數為: `min(total_count, max_freq+k)`
我們最多能有`max_freq+k`個字母, 但前提是不能超出window size

```
X X X X X X X X X X X X
```

因此這就是個(26n)的時間複雜度
```py
def characterReplacement(self, s: str, k: int) -> int:
    n = len(s)
    res = l = r = 0
    window = defaultdict(int)
    def check():
        total = mx = 0
        for v in window.values():
            mx = max(mx, v)
            total += v
        return mx, total
    while r < n:
        window[s[r]] += 1
        r += 1

        mx, total = check()
        while l < r and total-mx > k:
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            l += 1

            mx, total = check()
        res = max(res, min(r-l, mx+k))
    return res
```

但其實我們並不用每次都重新從hashmap裡計算個數
首先:
- 總個數可以透過`r-l`得知. [l,r) 左閉右開
- 我們就一直移動`r` pointer直到`r-l-max_freq > k`, 這時但表我們該收縮sliding window了
- 前面我們說到sliding window內的最高個數為`min(r-l, max_freq+k)`, 但仔細思考一下, 其實我們已經限制sliding window的大小不能超過k次替換, 所以sliding window size, `r-l`, 就是當次最佳解
- 那每個合法的sliding window下我們都能更新`res = max(res, r-l)`. 藉此找出全局最佳解
