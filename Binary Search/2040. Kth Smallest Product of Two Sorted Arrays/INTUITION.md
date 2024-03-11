# Intuition

一開始想到的是能不能像k merge sorted list那概念一樣
最小的肯定是nums1[0]*nums2[0], 但下一個是nums1[1]*nums2[0]還是nums1[0]*nums2[1]我們不知道
但由於有序的關係, 可以想成我們相當於有多個linked list
1. nums1[0]*nums2[0] -> nums1[0]*nums2[1] -> nums1[0]*nums2[2]
2. nums1[1]*nums2[0] -> nums1[1]*nums2[1] -> nums1[1]*nums2[2]
3. nums1[2]*nums2[0] -> nums1[2]*nums2[1] -> nums1[2]*nums2[2]
...

然後將每個linked list的頭放進minH裡, 這樣透過k次搜尋應當就能找出k-th smallest product
但由於這題有負數存在, 負數x負數可能會變成一個較大的正數, 這導致我們的linked list相互乘積不再是有序的

所以接著想, 是不是應該把負數部分跟正數部分拆開處理
nums1 = nums1_neg + nums1_pos
nums2 = nums2_neg + nums2_pos

這樣會有四種組合, 我們一樣想成乘積由小到大的linked list, 然後將該head of linked list放入pq
我們pq存放[
    product,
    index of nums1,
    index of nums2,
    1 means nums1_pos, -1 means nums1_neg
    1 means nums2_pos, -1 means nums2_neg
]

1. linked list of nums1_neg * nums2_neg: 逆序相乘才會是由小到大

```py
for i in range(len(nums1_neg)-1, -1, -1):
    if nums2_neg:
        heapq.heappush(pq, [nums1_neg[i]*nums2_neg[c-1], i, c-1, -1, -1])
```

2. nums1_pos * nums2_neg: 

```py
ex. nums1_pos=[1, 13], nums2_neg=[-12, -1]
for i in range(len(nums1_pos)):
    if nums2_neg:
        heapq.heappush(pq, [nums1_pos[i]*nums2_neg[0], i, 0, 1, -1])
```

3. nums1_neg * nums2_pos:

```py
for i in range(len(nums1_neg)):
    if nums2_pos:
        heapq.heappush(pq, [nums1_neg[i]*nums2_pos[d-1], i, d-1, -1, 1])
```

4. nums1_pos * nums2_pos:

```py
for i in range(len(nums1_pos)):
    if nums2_pos:
        heapq.heappush(pq, [nums1_pos[i]*nums2_pos[0], i, 0, 1, 1])
```

整體想法如下, 可惜這樣會**TLE**
原因是`k <= nums1.length * nums2.length <= 5*10^4 * 5*10^4`

```py
m, n = len(nums1), len(nums2)
nums1_neg, nums1_pos = [], []
for i in range(m):
    if nums1[i] < 0:
        nums1_neg.append(nums1[i])
    else:
        nums1_pos.append(nums1[i])
nums2_neg, nums2_pos = [], []
for i in range(n):
    if nums2[i] < 0:
        nums2_neg.append(nums2[i])
    else:
        nums2_pos.append(nums2[i])

pq = [] # min heap, [product, nums1_idx, nums2_idx, 1/-1 means nums1_pos/nums1_neg, 1/-1 means nums2_pos/nums2_neg]
a, b = len(nums1_neg), len(nums1_pos)
c, d = len(nums2_neg), len(nums2_pos)

for i in range(a-1, -1, -1):
    if nums2_neg:
        heapq.heappush(pq, [nums1_neg[i]*nums2_neg[c-1], i, c-1, -1, -1])
for i in range(b):
    if nums2_neg:
        heapq.heappush(pq, [nums1_pos[i]*nums2_neg[0], i, 0, 1, -1])
for i in range(a):
    if nums2_pos:
        heapq.heappush(pq, [nums1_neg[i]*nums2_pos[d-1], i, d-1, -1, 1])
for i in range(b):
    if nums2_pos:
        heapq.heappush(pq, [nums1_pos[i]*nums2_pos[0], i, 0, 1, 1])

while k:
    res, i, j, num1, num2 = heapq.heappop(pq)
    if num1 > 0 and num2 > 0: # nums1_pos * nums2_pos
        j += 1
        if j < len(nums2_pos):
            heapq.heappush(pq, [nums1_pos[i]*nums2_pos[j], i, j, num1, num2])

    elif num1 > 0 and num2 < 0: # nums1_pos * nums2_neg
        j += 1
        if j < len(nums2_neg):
            heapq.heappush(pq, [nums1_pos[i]*nums2_neg[j], i, j, num1, num2])

    elif num1 < 0 and num2 > 0: # nums1_neg * nums2_pos
        j -= 1
        if j >= 0:
            heapq.heappush(pq, [nums1_neg[i]*nums2_pos[j], i, j, num1, num2])
    elif num1 < 0 and num2 < 0: # nums1_neg * nums2_neg
        j -= 1
        if j >= 0:
            heapq.heappush(pq, [nums1_neg[i]*nums2_neg[j], i, j, num1, num2])
    k -= 1
return res
```

既然線性不行, 那麼這個`k`也只能用binary search去猜了
我們可以去猜測k-th smallest product為`mid`, search space為[
    min(nums1_pos[0]*nums2_pos[0], nums1_pos[-1]*nums2_neg[0], nums1_neg[0]*nums2_pos[-1], nums1_neg[-1]*nums2_neg[-1]),
    max(nums1_pos[-1]*nums2_pos[-1], nums1_pos[0]*nums2_neg[-1], nums1_neg[-1]*nums2_pos[0], nums1_neg[0]*nums2_neg[0]),
]
或者search space就直接根據constraint去設: -10^5 <= nums1[i], nums2[j] <= 10^5

我們就檢查乘積`<= mid`的值有多少個, 是不是`>=k`個
是的話`mid`就在往小裡猜, 但如果小於`k`個的話, 那麼mid就得猜得更大一點

整體框架如下:
```py
l, r = -1e10, 1e10
while l < r:
    mid = l + (r-l)//2
    if count(mid) < k:
        l = mid+1
    else:
        r = mid
return l
```

由於nums1, nums2都是有序的, 所以也可以透過遍歷nums1[i] + binary search來找出合適的nums2[j]個數

```py
def count(m):
    cnt = 0
    for num in nums1:
        if num > 0:
            # num * nums2[j] <= m
            # nums2[j] <= m/num
            # [0,j]都是符合的
            cnt += bisect_right(nums2, floor(m/num))
        elif num < 0:
            # num * nums2[j] > m
            # nums2[j] > m/num
            # [ceil(m/num), nums2[-1]] 都是符合的 => [j, n-1]
            cnt += len(nums2)-bisect_left(nums2, ceil(m/num))
        else: # product == 0
            if m >= 0:
                cnt += len(nums2)
    return cnt
```