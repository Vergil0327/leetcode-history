"""
brute force:
```py
class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        s = list(sorted(set(nums)))

        res = 0
        for num in nums:
            for t in s:
                if num%t == 0:
                    res += t
                    break
        return res
```

很直覺的想法是兩個迴圈遍歷, 但這樣明顯會TLE
所以我們可以反過來想

我們要最小的和
所以由小到大遍歷, 把能被整除的陸續處理掉並做上記號避免反覆計算即可
利用hashmap可以將處理後的nums[i]個數加到當前的因數上

那麼最後只要看留在hashmap裡的值, 各是多少個數即知道總和
"""

class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        s = list(sorted(set(nums)))

        count = Counter(nums)
        processed = set()
        
        mx = s[-1]
        for t in s:
            if t in processed: continue
            processed.add(t)

            x = 2
            while (cur := t * x) <= mx:
                processed.add(cur)
                if cur in count:
                    count[t] += count[cur]
                    del count[cur]
                x += 1
        return sum(num * x for num, x in count.items())


