# Intuition

由於是要維護一個長度為k的subarray, 首先想到的是sliding window
並且又要求整個window是有序的，這樣才能高效地知道第x個小的數是多少
所以我們用sorted list來維護這個window

time complexity: $O(nlogn)$

# Other Solution

但這題還有個更聰明的解法是:
我們可看到數據範圍: `-50 <= nums[i] <= 50`

所以我們可以把數據平移一下變成: `0 <= nums[i] <= 100`
然後用長度為50的bucket來儲存負數的的個數: `counter[nums[i]+50] = count`

等到sliding window長度滿足k的時候，我們便遍歷`counter`這個大小為50的bucket

一但`count >= x`, 此時的遍歷的數便為第x小的數

```py
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        counter, res = [0] * 50, [0] * (n - k + 1)
        OFFSET = 50
        for i in range(n):
            # 這兩行用來維護長度固定為k的sliding window
            if nums[i] < 0: counter[nums[i] + OFFSET] += 1
            if i-k >= 0 and nums[i-k] < 0: counter[nums[i-k]+OFFSET] -= 1
            if i - k + 1 < 0: continue 

            count = 0
            for j in range(50):
                count += counter[j]
                if count >= x:
                    res[i - k + 1] = j - 50
                    break
        return res
```