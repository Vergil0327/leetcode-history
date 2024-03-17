# Intuition

目的就是要找出一段subarray使得frequency_max-frequency_min <= k
所以我們先找出所有frequency, 並排序:
    
```py
freq = list(sorted(Counter(word).values()))
```

那再來我們就用sliding window 找出每一段合法subarray使得freq[r]-freq[l] <= k

```
X X X {X X X X X X X X X} X X X 
       l               r
```

那這樣我們要刪除的字符就是前面prefix刪掉跟後面suffix每個frequency刪成freq[l]+k (我們只需將後面高freq刪到跟nums[l]相差<=k即可)

所以前面prefix刪除的份就是sum(freq[0:l-1])
後面suffix刪除的字符數就是sum(freq[r+1:n-1]) - (freq[l]+k) * len(n-r)

因此我們維護一個prefix sum跟suffix sum, 分別是`pre_deleted`, `sufsum`
然後再進行sliding window時維護這兩個變數即可

```py
freq = list(sorted(Counter(word).values()))
n = len(freq)

res = len(word)
pre_deleted = j = 0
sufsum = sum(freq)
for i in range(n):
    # X X X {X X X X X X X} X X X
    #        i              j     n
    while j < len(freq) and freq[j]-freq[i] <= k:
        sufsum -= freq[j]
        j += 1
        
    suf_deleted = sufsum - (freq[i]+k)*(n-j)
    res = min(res, pre_deleted + suf_deleted)
    pre_deleted += freq[i]
return res
```