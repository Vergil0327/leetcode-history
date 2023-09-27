# Intuition

首先想到的是可以計算prefix sum來比較好知道segment sum

nums = [1,2,5,6,1]
presum = [1,3,8,14,15]

再來看每次queries[i]:
queries[0]: [0,2,5,6,1]
queries[1]: [0,2,5,0,1]
queries[2]: [0,2,0,0,1]
queries[3]: [0,2,0,0,0]

如果一開始區間是[l,r]=[0,n-1]
那麼queries[i]會分成兩個segment:
1. [l, removeQueries[i]-1] removeQueries[i]
2. [removeQueries[i]+1, r]

segment sum也會從presum[r]-presum[l-1]變成:
1. presum[removeQueries[i]-1]-presum[l-1]
2. presum[r]-presum[removeQueries[i]]

所以如果我們用個max heap來維護segment_sum的話, 就能用O(1)時間得知queries[i] = -maxHeap[0]

再來就是想該如何順利拆分max heap裡的target segment.

*constraint: All the values of removeQueries are unique.*

如果當前removeQueries[i]落在當前的max segment區間內, 那我們就要進行拆分.
如果我們用SortedList來存這些區間的話, 就可以用binary search來找出當前removeQueries[i]所影響的segment然後進行拆分
這樣在拆分完後, 將原本的區間移除, 再將兩個新的區間加入到maxHeap裡, 如此一來就又能得到當前res[i] = -maxHeap[0][0]

由於我們需要將原本的區間移除, 單純的maxHeap並不支援快速查找的功能, 所以得同樣利用有序容器SortedList這類的數據結構來

那這樣對於眾多segments來說: Sorted Segments [l, r, sum], ...
對於當前的removeIdx, 我們可以用bisect_right(removeIdx)-1找出該需要拆分的segment

```py
# sl: SortedList stores [l, r, sum]
j = sl.bisect_right((idx, inf, inf))-1
l, r, tot = sl.pop(j)
```

拆分後的leftSum跟rightSum如下, 並記得重新加入到sorted segments裡:
```py
tot -= nums[idx]
rightSum = presum[r]-presum[idx]
leftSum = tot-rightSum

sl.add((l, idx-1, leftSum))
sl.add((idx+1, r, rightSum))
```

至於查找當前max segment sum也是一樣
先把當前未拆分的segment sum移除, 然後加入拆分後的leftSum, rightSum後即可以O(1)時間找出
```py
sortedSum.remove(tot)

# ... calculate leftSum, rightSum

sortedSum.add(leftSum)
sortedSum.add(rightSum)
res[i] = sortedSum[-1]
```

time: $O(nlogn)$

# Other Solution - Union-Find

這想法是我們從最後的結果往回倒推回來
當我們從後往前將removeQueries加回來後, 跟左右segment互相union在一起
由於segment sum只會越來越大, 所以我們持續將當前segment sum跟前一個max segment sum取max即可
如此一來就能依序得到當前最大的max segment sum

```
nums = [0, 0, 0, 0, 0, 0]
nums = [0, 0, 0, 5, 0, 0]
nums = [0, 0, 0, 5, 0, 1]
nums = [0, 0, 0, 5, 2, 1]
...
```

對於`removeQueries[i]`來說:
- 加回來前的max segment sum為res[i]
- 所以加回來後的為res[i-1] = max(res[i], segment_sum[find(removeQueries[i])])

time: O(n) approximately