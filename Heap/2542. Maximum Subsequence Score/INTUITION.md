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