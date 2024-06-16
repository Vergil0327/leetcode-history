很明顯的, 由於nums會隨著queries[i]改變, 會隨時間變化的區間查詢
那就是利用segment tree並即時更新維護

所以一開始先建立segment tree
```py
n = len(nums)
        
count = [0]
for i in range(1, n-1):
    count.append(int(nums[i-1] < nums[i] and nums[i] > nums[i+1]))
count.append(0)

seg = SegmentTree(count, op=sum)
```


然後依據題意即時更新segment tree即可
對於每次更新`nums[i] = val`
由於nums[i]會連帶影響到nums[i-1]跟nums[i+1]還是不是peak
每次都要更新維護**nums[i-1]**, **nums[i]**跟**nums[i+1]**

至於搜索[l, r]之間有多少peak, 由於邊界的`l`跟`r`肯定不是peak
所以我們對於[l,r]區間, 我們應該搜索segment tree的[l+1, r-1]即可
以防`l`跟`r`本身是peak, 但由於位於該次query的邊界而不算在內

```py
res = []
for q in queries:
    if q[0] == 1:
        l, r = q[1], q[2]

        res.append(seg.query(l+1, r-1))
    else:
        idx, val = q[1], q[2]
        nums[idx] = val
        if idx-1>=0:
            seg[idx-1] = int((nums[idx-2] < nums[idx-1] if idx-2 >=0 else False) and nums[idx-1] > nums[idx])

        seg[idx] = int((nums[idx-1] < nums[idx] if idx-1>=0 else False) and (nums[idx] > nums[idx+1] if idx+1<n else False))
        
        if idx+1<n:
            seg[idx+1] = int(nums[idx] < nums[idx+1] and (nums[idx+1] > nums[idx+2] if idx+2<n else False))

return res

```