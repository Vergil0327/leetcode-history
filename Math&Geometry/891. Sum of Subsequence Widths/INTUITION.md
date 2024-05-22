# Intuition

既然關心的是min/max, 而且我們要找的是subseq.
感覺能試試sorting, sorting後再去取subseq一樣能取出原本nums的2^n種 (每個元素可取可不取)
 
nums = [2,1,3] => sort => [1,2,3]
那這樣我們就能以O(n^2)確定出min/max element位置
那麼這時**width = max-min**也知道了, 再來就看能貢獻這個width的subseq有多少個
假設min element = nums[l], max element = nums[r],
既然是subseq., 兩element內的元素我們都可取可不取, 所以總共會有pow(2, r-l-1)種subseq.

```py
nums.sort()
res = 0
for l in range(n):
    for r in range(l+1, n):
        res += pow(2, r-l-1) * (nums[r]-nums[l])
return res
```

這時我們就找到了O(n^2)的解法, 但依照這題的數據規模是過不了的
我們得將複雜度降至O(n), 那這時我們資訊就只剩nums[i]

由於我們排序過, 我們遍歷的nums[i]如果作為min element, 那麼nums[i]的右半邊元素都可以作為max element
如果作為max element, 那麼nums[i]的左半邊都是min element

所以我們拆開來看:
1. 以nums[i]作為min element, 那麼右邊就會有n-i-1個max element
2. 以nums[i]作為max element, 那麼左邊就會有i個min element

我們要求的width = max - min for each subseq.
那就相當於全部subseq.的max減去全部subseq.的min

`answer = sum(max of each subseq.) - sum(min of each subseq.)`

結合上面, 我們其實就計算每個 nums[i]作為max element的貢獻度 - nums[i]作為min element的貢獻度即可
1. 以nums[i]作為max element貢獻度: nums[i] * 2^i (i個元素可取可不取, 每個組成的subseq.的min element都會是nums[i])
2. 以nums[i]作為min element貢獻度: nums[i] * 2^(n-i-1)

全部加總起來再對1e9+7取餘, 即為答案