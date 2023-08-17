# Intuition

如果是brute force的話，我們可以透過 dfs(i, k, currSum, currMin) 遞歸求出答案
但如果我們對nums2[i]由大到小排序的話，由於持續取`min`，因此currMin肯定是當前的nums2[i]
如此一來我們就可以直接用O(1)時間找出currMin

因此對nums2[i]的數值排序或許會有幫助，從這邊再繼續想
要跟currMin(=nums2[i])相乘的是長度為`k`的subsequence和，由於是subseq.
代表我們其實不用管位置順序，只要在當前為止的前`i`個裡(也就是在arr[:i]中)，找出`k`個最大的值即可

既然是要維護前`k`個最大的數，那我們可以想到利用priority queue來幫我們以O(nlogk)時間維護當前i個裡前`k`個值最大的數

# Approach

1. 首先我們對nums2[i]的值由大到小排序，方便我們找出當前要相乘的 `currMin`
2. 再來我們維護一個 `minHeap`，持續把`nums[1]`加入到`minHeap`中
3. 並且為了省去`sum(minHeap)`的時間，我們用一個變數`currSum`來維護當前`minHeap`裡的總和
   1. 一但 `len(minHeap) > k`，我們便pop掉最小的值，並且 `currSum -= heappop(minHeap)`
   2. 對於當前`i`位置來說，一但`len(minHeap) = k`，代表我們找到一段長度為`k`並且由前k個最大的值組成的subsequence，其分數為 `currSum * currMin`

# Complexity

- time complexity
$$O(nlogn + nlogk)$$

- space complexity

$$O(n)$$

# Other Intuition

由於有兩個變因，先試著想有沒有辦法使得其中一個變因只需要用O(1)時間知道

首先想到的是如果將nums2由大到小排列, 那麼nums2[i]永遠都會是該subseq.的min

```
ex.1
nums1 = [2 3 1] 3
nums2 = [4 3 2] 1
          k個
```

這樣下一回合加進[3,1] [nums1, nums2] pair後, 由於這時min nums2[i]一定是1
所以我們應該從上一輪k個裡面踢出nums1最小的一個

所以我們先對(nums2, nums1) pair最由大到小排序
再來再透過min heap持續找出最小的踢出並維持k-size

最終找出全局最高分數即可

```py
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        arr = sorted(zip(nums2, nums1), reverse=True)
        minHeap = []
        tot = 0
        for i in range(k):
            tot += arr[i][1]
            heapq.heappush(minHeap, arr[i][1])

        res = arr[k-1][0] * tot
        for i in range(k, n):
            tot += arr[i][1]
            tot -= heapq.heappop(minHeap)
            res = max(res, tot * arr[i][0])
            
            heapq.heappush(minHeap, arr[i][1])
        return res
```