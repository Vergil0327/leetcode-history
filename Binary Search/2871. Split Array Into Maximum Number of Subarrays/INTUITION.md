# Intuition

由於AND這操作是取共同的bit位, 因此越AND值肯定會越小
所以最小的AND score必定是將全部nums[i]全AND起來

```py
minAND = nums[0]
for i in range(1, n):
    minAND &= nums[i]
```

再來對於極值, 我們可以試著看能不能用binary search來找出這個值, 框架如下
search space: 最少一個subarray, 最多n個, [1, n]
```py
l, r = 1, n
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

那這個check helper func也很簡單
由於最小score已經知道是`minAND`, 因此如果我們用binary search猜說能不能分成`mid`個subarray
代表每個subarray的score必須小於`minAND/mid`, 因此我們就用greedy的方式去找即可

我們紀錄當前合法subarray的數目為`cnt`
我們持續對nums[i]進行**bitwise-AND**操作, 一但當前subarray score <= minAND/mid, 那就`cnt+=1`
最後看能不能找到大於等於`mid`個合法subarray, 也就是`cnt >= mid`即可

```py
def check(mid):
    target = minAND/mid

    cur = nums[0]
    cnt = 0
    for i in range(n):
        cur &= nums[i]
        if cur <= target:
            cnt += 1
            if i+1 < n:
                cur = nums[i+1]
    return cnt >= mid
```

# Other Solution

[lee215](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/solutions/4109955/java-c-python-one-pass-count-zero-score/)
[greedy approach](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/solutions/4109980/python-greedy-o-n/)