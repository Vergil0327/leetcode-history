# Intuition

目標是min(sum(pow(nums1[i]-nums2[i], 2) for i in range(n)))

首先, 因為對於每個pair, 我們可以調整nums1[i]往nums2[i]靠，或反過來讓nums2[i]往nums1[i]靠來降低sqaure
所以我們並不關心我們是用k1去調整nums1[i]或是用k2來調整nums2[i]
k=k1+k2

並且對於每個pair, 我們只關心他們的diff=nums1[i]-nums2[i], 降低diff就能降低square
所以首先可以先往greedy想, 優先把高的square降下來
=> 用max heap優先降低diff大的 => 但假如有多個相同max diff的話, 一個一個降會TLE

```py
def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
    n = len(nums1)
    mxHeap = [] # store diff=nums1[i]-nums2[i]
    k = k1+k2
    for i in range(n):
        mxHeap.append(-abs(nums1[i]-nums2[i]))
    heapq.heapify(mxHeap)
    
    while k and mxHeap:
        diff = -heapq.heappop(mxHeap)
        if diff-1 > 0:
            heapq.heappush(mxHeap, -(diff-1))
        k -= 1
    return sum(pow(num, 2) for num in mxHeap)
```

所以這邊我們先用hashmap記錄每個diff有多少個, 然後在後面部分同時處理

1. 先找出max diff, 然後把其他也是max diff的pair挑出來後看有多少個
```py
while k:
    diff, cnt = mxHeap[0][0], mxHeap[0][1]
    if diff == 0: break
    diff, cnt = mxHeap[0][0], mxHeap[0][1]
    if diff == 0: break

    # merge same diff pair with current
    heapq.heappop(mxHeap)
    while mxHeap and mxHeap[0][0] == diff:
        _, cnt2 = heapq.heappop(mxHeap)
        cnt += cnt2
```
2. 然後開始操作
    - 如果 k >= cnt, 那麼每個diff都能-1
        - heapq.heappush(mxHeap, [diff+1, cnt])
        - k -= cnt
    - 如果 k < cnt, 那麼有k個pair可以diff-1, 剩下的cnt-k則維持不變
        - heapq.heappush(mxHeap, [diff, cnt-k])
        - heapq.heappush(mxHeap, [diff+1, k])
        - k = 0