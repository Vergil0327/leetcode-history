# Intuition

find interval.size between each non-decreasing element

5,3,4,4,7,3,6,11,8,5,11 => non-decreasing = 5, 7, 11, 11
between each non-decreasing element, max size is the answer what we want

be cautious of this situation: nums=[10,1,2,3,4,5,6,1,2,3], expected=6
each **decreasing array** will remove element **simultaneously**

1. 10,1,2,3,4,5 => 10,2,3,4,5 => 10,3,4,5 => 10,4,5 => 10,5 => 10
2. 6,1,2,3      => 6,2,3      => 6,3      => 6
3. => 10, 6 => 10

會發現會發現如果有多段non-decreasing array, 如果每段non-decreasing array的首個element如果符合條件, 靠前的non-decreasing仍會逐漸移除掉後面的head of non-decreasing array

所以直覺上能想到我們可以從後往前處理, 這樣一但靠後的non-decreasing array也符合移除條件
我們也會在之後靠前的non-decreasing array一併處理

所以我們可以由後往前遍歷, 並利用stack儲存遍歷過的element
一但符合`nums[stack[-1]] < nums[i]`這條件, 就代表我們找到一段可以移除的區間能形成non-decreasing array

這時有3種情況, 其中*為移除的元素:

1. nums[i] * * * * nums[stack[-1]] * * *
    - 如果nums[i] <= nums[stack[-1]]: res = max(4, 3)
    - 如果nums[i] > nums[stack[-1]]: 這情形我們還需多一步來除掉nums[stack[-1]], res = max(4+1, 3)
2. nums[i] * * * nums[stack[-1]] * * *
    - 如果nums[i] <= nums[stack[-1]]: res = max(3, 3)
    - 如果nums[i] > nums[stack[-1]]: 那麼我們可以再多一步讓nums[i]移除掉nums[stack[-1]], res = max(3+1, 3)
3. nums[i] *  nums[stack[-1]] * * *:
    - 如果nums[i] <= nums[stack[-1]]: res = max(1, 3)
    - 如果nums[i] > nums[stack[-1]]: res = max(1, 3) nums[stack[-1]]不會多佔用我們一次移除

當時就卡在這, 但實際上我們可以定義:
dp[i]: the removed elements from i to the right
那麼一但我們在遍歷過程中, 符合`nums[i] > nums[stack[-1]]`這條件, 就代表我們能讓nums[i]移除掉nums[stack[-1]]這段, 並包含nums[stack[-1]]所以除掉的部分
所以代表我們能更新dp

### 狀態轉移

1. 對於nums[i]來說, 他可以花一步吃掉nums[stack[-1]]
    - dp[i] = dp[i]+1
2. 但如果dp[nums[stack[-1]]]的移除數量較多, 也就是上面的第三種情形, 會發現nums[i]吃掉nums[stack[-1]]這部會同步發生在nums[stack[-1]]移除元素的過程中, 所以
    - dp[i] = max(dp[i], dp[stack.pop()]) # 直接stack.pop(), 因爲nums[stack[-1]]會被nums[i]吃掉

所以整體框架為:
```py
for i in range(n-1, -1, -1):
    while stack and stack[-1] < nums[i]:
        dp[i] = max(dp[i]+1, dp[stack.pop()])
    stack.append(i)
```

由於最多步數可能開始於任意一個元素, 所以最終答案就是: `max(dp)`


# Intuition 2

另外有一種方法是直接去模擬整個程序

對於nums = [l * * * * * r * * * * rr]

首先我們找出我們可以removed的subarray, [l, r], r為能被nums[l]吃掉的元素

```py
queue = deque() # removed interval [l, r]
for i in range(n-1, 0, -1):
    if nums[i-1] > nums[i]:
        queue.append([i-1, i])
```

然我們就開始逐步BFS模擬, 每當nums[l] 吃掉 nums[r]
我們就要再從nums[r]再繼續往後找下個能被nums[l]移除的元素

```py
rr = nextPos[r]
while rr < n and rr in removed:
    rr = nextPos[rr]
nextPos[r] = rr # 找到後記得回頭更新next[r], 以避免反覆搜索這段區間
```

所以整體框架如下, 等到BFS無法再繼續下去, 代表已無區間可以刪除

```py
removed = set()
step = 0
while queue:
    for _ in range(len(queue)):
        l, r = queue.popleft()

        if l in removed: continue
        removed.add(r)

        # find next element for nums[l] to remove
        rr = nextPos[r]
        while rr < n and rr in removed:
            rr = nextPos[rr]
        nextPos[r] = rr # update

        if rr < n and nums[l] > nums[rr]: # keep removing if we found valid nums[rr] for nums[l] to remove
            queue.append([l, rr])
    step += 1
return step
```