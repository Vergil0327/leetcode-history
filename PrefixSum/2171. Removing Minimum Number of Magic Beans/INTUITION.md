# Intuition

由於無法增加數字, 所以所有小於equal number的beans[i]都只能移除到0為止
所以直覺想到的是我們可以從數量大到小遍歷, 持續移除
所以當選擇arr[i]作為equal number時, 由大到小累積的移除數量 + prefix sum即為我們總移除數
遍歷一遍全局取小即為答案

所以用prefix sum跟accumuate兩個變量來幫助計算

排序後從後往前遍歷(亦即數字由大到小)
當我們equal number從nums[i]變為nums[i-1]時:
- accumulate += (nums[i]-nums[i-1]) * (# of nums[i])
- \# of nums[i-1]數量要加上 # of nums[i]

只要持續維護好accumulate然後再加上prefix sum, 我們就能以O(n)時間計算出將每個nums[i]當作magic beans所需的移除操作數

edge case: 當beans.size == 1時, 無需任何操作, 直接返回0即可

# Concise & Optimization - Math Solution

- 直接對beans由小到大排序
- beans[i]之前都必須移除到0為止
- beans[i+1]開始到之後都必須移除到beans[i]為止

- 也就是要將beans[i]轉化成[0, 0, 0, ...., beans[i], beans[i], ..., beans[i]] => removal = sum(beans) - beans[i] * (n-i)

所以當equal number等於beans[i]時, 當前需要的移除操作數 = sum(beans) - (n-i) * beans[i]


```py
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        total = sum(beans)
        res = total
        for i in range(n):
            curr_removal = total-beans[i]*(n-i)
            res = min(res, curr_removal)
        return res
```