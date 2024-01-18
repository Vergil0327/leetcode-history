# Intuition

subarray => sliding window or prefix sum?

threshold/k => [threshold/1, threshold/2, threshold/3, threshold/4, ...]

我們僅需返回任意合法`k`

我們能簡單想到的有
- k越大 => min(subarray)數值門檻越低

- 對於一個合法的subarray => min(subarray) > threshold/subarray.length

也就是**subarray.length > threshold / min(subarray)**

一個個來看:
k=1: [X]
如果不滿足`min(subarray) > threshold / subarray.length`, 那在往後看

k=2: [X] Y
min(min(subarray), Y) > threshold / (subarray.length+1)

我們關心的只有min(subarray)

對於每個nums[i], 我們找出如果nums[i]是min(subarray), subarray.length可以是多少(也就是左右可延伸多少)

也就是如果知道`prevSmaller[i]`, `nextSmaller[i]`的話:
- subarray.length = nextSmaller[i]-prevSmaller[i]-1
- min(subarray) = nums[i]
- 我們只要判斷這個條件: min(subarray) * subarray.length > threshold => nums[i] * (nextSmaller[i]-prevSmaller[i]-1) > threshold, 假如成立那就是合法subarray

所以我們只要遍歷一遍nums[i], 然後看有沒有符合`nums[i] * (nextSmaller[i]-prevSmaller[i]-1) > threshold`這個條件即可

至於`nextSmaller[i]`跟`prevSmaller[i]`, 我們可以用monotonic stack來找

1. nextSmaller: 單調遞減的stack

```py
nextSmaller = [n]*n
stack = []
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] > num:
        nextSmaller[stack.pop()] = i
    stack.append(i)
```

2. prevSmaller: 單調遞增的stack

```py
prevSmaller = [-1]*n
stack = []
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] > num:
        stack.pop()

    if stack:
        prevSmaller[i] = stack[-1]
    stack.append(i)
```

3. 遍歷nums[i] 找出合法subarray

```py
for i in range(n):
    if nums[i] * (size := nextSmaller[i]-prevSmaller[i]-1) > threshold:
        return size
return -1
```

# Complexity

- time complexity: $O(n)$
- space complexity: $O(n)$