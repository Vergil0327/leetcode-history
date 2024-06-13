# Intuition

brute force solution: O(nlogn + klogn)
將每個(nums[i], nums[i+1]) pair放入 min heap裡
對nums[i]來說, i+1, i+2, i+3, ...所形成的pair會是non-decreasing
就在透過heap來讓我們快速查找即可

=> 可惜會TLE => 因為 k <= n*(n-1)/2 => 會高達10^8級別

```py
n = len(nums)

nums.sort()
minH = []
for i in range(n-1):
    heapq.heappush(minH, [nums[i+1]-nums[i], i, i+1])

res = 0
while k:
    res, i, idx = heapq.heappop(minH)
    if (j := idx+1) < n:
        heapq.heappush(minH, [nums[j]-nums[i], i, j])
    k -= 1
return res
```

那換個想法, k-th largest/smallest 這類題目, 都可以用binary search去猜看看
那麼題目就會轉換成: 如何判斷當前binary search猜的值太大過太小

我們試著直接去猜k-th smallest distance
distance range: [0, nums[-1]-nums[0] after sorting]
那這樣題目就變成進行binary search時, 如果能知道當前distance `mid`比多少pair還大時
我們就知道binary search該怎麼縮小範圍了

```py
nums.sort()
l, r = 0, nums[-1]-nums[0]

while l < r:
    mid = l + (r-l)//2
    if count(mid) <= k:
        l = mid
    else:
        r = mid-1
return l
```

再來就考慮這個helper function `count(mid)`

遍歷每個nums[i]去找出所有 <= mid的所有pair
暴力解會是O(n^2), 但由於我們已經知道要<= mid而且我們已排序過nums
可以透過binary search找出每個nums[i]能跟多少pair去組成 <= mid的pair

對於nums[i]來說, 他的上限pair為nums[i] + mid
透過`j = bisect_right(nums, mid+nums[i])`可得到會超出`mid`的pair位置`j`
所以能組成的pair為`j-1 - i` ([i+1, j-1]這範圍都可以跟nums[i]組成距離小於等於mid的pair)
示意圖如下:
```
{X X X X X X} X X X
 i            j
```

```py

def count(mid):
    cnt = 0
    for i in range(n):
        j = bisect_right(nums, mid+nums[i])
        cnt += max(0, (j-1)-i)
    return cnt
```