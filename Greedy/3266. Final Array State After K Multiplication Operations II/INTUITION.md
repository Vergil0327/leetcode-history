# Intuition

直覺想到利用heap, klog(n)解法

```py
mod = 10**9 + 7
arr = [[num, i] for i, num in enumerate(nums)]
heapq.heapify(arr)

while k:
    num, i = heapq.heappop(arr)
    heapq.heappush(arr, [num*multiplier, i])
    k -= 1

for num, i in arr:
    nums[i] = num%mod
return nums
```

但由於constraint: 1 <= k <= 10^9 => TLE
看來時間上不允許我們模擬整個操作過程

```
Input: nums = [2,1,3,5,6], multiplier=2

["2*2",2,3,5,6]
[4,"2*2",3,5,6]
[4,4,"3*2",5,6]

# 從這開始循環
["4*2",4,6,5,6]
[8,"4*2",6,5,6]
[8,8,6,"5*2",6]
[8,8,"6*2",10,6]
[8,8,12,10,"6*2"]

["8*2",8,12,10,12]
[16,"8*2",12,10,12]
[16,16,12,"10*2",12]
[16,16,"12*2",20,12]
[16,16,24,20,"12*2"]

... 反覆循環, 依序作用在index, [0,1,3,2,4], 持續循環
```

從上面可得知整個過程會持續循環
當min(nums) > max(nums)時, 是整個循環的開始

所以概念上會是:
1. 先模擬操作, 直到min(nums) * multiplier > max(num)
2. greedily反覆循環操作到剩餘的`k'`操作上

# Approach

所以首先我們先把開始循環前的操作消耗掉
- 找出`mn=min(nums)`以及`mx=max(nums)`的index作為key, 並配合SortedList模擬操作
- 持續操作直到下一步操作會: `mn*mul > mx`
- 並記得判斷一下如果`k`已經為0, 直接返回答案

```py
mod = 10**9 + 7
sl = SortedList([num, i] for i, num in enumerate(nums))

mnIdx, mxIdx = sl[0][1], sl[-1][1]
def check(sl):
    if sl[0][1] != mnIdx: return True

    target = -1
    for num, i in sl:
        if i == mxIdx:
            target = num
            break
    return sl[0][0] * mul <= target
    
while k and check(sl):
    k -= 1
    num, i = sl.pop(0)
    sl.add([num*mul, i])

if k == 0:
    for num, i in sl:
        nums[i] = num%mod
    return nums
```

再來就是找出完整的一次循環, 一樣利用heap模擬操作並記錄我們作用的index
一但我們紀錄的order開始循環時, 也就是滿足`if len(order)%2 == 0 and order[:len(order)//2] == order[len(order)//2:]`
這時我們就知道完整的循環順序為: `order[:len(order)//2]`

```py
order = []
while k:
    k -= 1
    num, i = sl.pop(0)
    sl.add([num*mul, i])
    order.append(i)

    if len(order)%2 == 0 and order[:len(order)//2] == order[len(order)//2:]:
        break
if k == 0:
    for num, i in sl:
        nums[i] = num%mod
    return nums
```

再來就是找出**循環次數**以及**剩餘操作次數**, 並作用在nums上即可

```py
order = order[:len(order)//2]
n = len(order)

q, r = divmod(k, n)
for _ in range(r):
    num, i = sl.pop(0)
    sl.add([num*mul, i])

for num, i in sl:
    nums[i] = num * pow(mul, q, mod) % mod
return nums
```