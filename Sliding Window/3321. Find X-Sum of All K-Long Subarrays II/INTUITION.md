# Intuition

這是[3318. Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/)的follow-up, 數據規模變大了

從數據規模上, 看起來必須是O(n)或是O(nlogn)

從brute force來看 (如下所示):

O(n)時間的sliding window是必須的, 那再來要優化的方向
應該就是如何維護top x items的frequency排序及其總和

```py
# brute force
def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    n = len(nums)
    answer = [-1] * (n-k+1)

    count = Counter()
    for i in range(k-1):
        count[nums[i]] += 1

    for i in range(k-1, n):
        count[nums[i]] += 1
        arr = list(sorted([[v, k] for k, v in count.items()], reverse=True))
        answer[i-k+1] = sum(v*k for v, k in arr[:x])
        count[nums[i-k+1]] -= 1
    return answer
```

為了維護frequency, 首先想到有序容器SortedList
我們利用兩個SortedList, `topX`跟`other`, 來維護**前X元素**及**其他元素** (如下所示)
如此一來, 只要我們能再進一步優化計算x-sum的方式, 如果能以O(1)時間計算的話
這題就算是結束了

```py
from sortedcontainers import SortedList
def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    n = len(nums)
    answer = [-1] * (n-k+1)

    count = Counter()
    for i in range(k-1):
        count[nums[i]] += 1

    topX = SortedList()
    other = SortedList([(count[num], num) for num in set(nums)])
    while other and len(topX) < x:
        topX.add(other.pop())
    for i in range(k-1, n):
        # add new item to sliding window after removing outdated item
        old_item = (count[nums[i]], nums[i])
        if old_item in topX:
            topX.remove(old_item)
        else:
            other.remove(old_item)
            
        count[nums[i]] += 1
        item = (count[nums[i]], nums[i])
        topX.add(item)
        while topX and len(topX) > x:
            other.add(topX.pop(0))

        # calculate X sum
        answer[i-k+1] = sum(num*freq for freq, num in topX)

        # remove old item from sliding window
        old_item = (count[nums[i-k+1]], nums[i-k+1])
        if old_item in topX:
            topX.remove(old_item)
        else:
            other.remove(old_item)

        count[nums[i-k+1]] -= 1
        other.add((count[nums[i-k+1]], nums[i-k+1]))
        while other and len(topX) < x:
            topX.add(other.pop())
    return answer
```

因此下一步就來看如何維護x-sum
其實就是在所有會影響到`topX`這個有序容器的地方, 依照新增/移除的情境去維護x-sum即可

```py
from sortedcontainers import SortedList
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [-1] * (n-k+1)

        count = Counter()
        for i in range(k-1):
            count[nums[i]] += 1

        topX = SortedList()
        other = SortedList([(count[num], num) for num in set(nums)])
        while other and len(topX) < x:
            topX.add(other.pop())

        sumX = sum(num*freq for freq, num in topX)

        for i in range(k-1, n):
            # add new item to sliding window
            old_item = (count[nums[i]], nums[i])
            if old_item in topX:
                topX.remove(old_item)
                sumX -= old_item[0]*old_item[1] # only item in topX effect sumX
            else:
                other.remove(old_item)
                
            count[nums[i]] += 1
            item = (count[nums[i]], nums[i])
            topX.add(item)
            sumX += item[0]*item[1]
            while topX and len(topX) > x:
                sumX -= topX[0][0] * topX[0][1] # only item in topX effect sumX
                other.add(topX.pop(0))

            # O(1) X sum
            answer[i-k+1] = sumX

            # remove old item from sliding window
            old_item = (count[nums[i-k+1]], nums[i-k+1])
            if old_item in topX:
                topX.remove(old_item)
                sumX -= old_item[0]*old_item[1] # only item in topX effect sumX
            else:
                other.remove(old_item)

            count[nums[i-k+1]] -= 1
            other.add((count[nums[i-k+1]], nums[i-k+1]))
            while other and len(topX) < x:
                sumX += other[-1][0] * other[-1][1] # only item in topX effect sumX
                topX.add(other.pop())
        return answer
```