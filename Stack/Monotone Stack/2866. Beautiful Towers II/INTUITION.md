# Intuition

想法是遍歷所有可能peak `i` from 0 to n-1

如果我們能知道:
- left[i]: the maximum possible sum of heights considering maxHeights[:i]
- right[i]: the maximum possible sum of heights considering maxHeights[i:]

由於left[i]跟right[i]都包含maxHeights[i], 所以根據排容原理, 我們再額外扣除maxHeights[i]
那麼answer = max(left[i] + right[i] - peak for peak in range(n))

所以再來想看看有沒有辦法求出**left**跟**right** array

3 5 10 11 12 9 2 7
j i
prevSmaller[i] = j => [j+1:i]這段都是maxHeights[i] = maxHeights[i] * (i-j) + left[j]

6 5 10 11 12 9 2 7
  j          i
prevSmaller[i] = j => [j+1:i]這段都是maxHeights[i] = maxHeights[i] * (i-j) + left[j]

所以可以用monotonically stack來求得left[i]

```py
left = [0] * n
stack = [-1]
for i in range(n):
    while len(stack) > 1 and maxHeights[stack[-1]] >= maxHeights[i]:
        stack.pop()
    j = stack[-1]
    left[i] = (i-j) * maxHeights[i] + (left[j] if j >= 0 else 0)
    stack.append(i)
```

同理, right[i]就改從右往左用monotonical stack來求

```py
right = [0] * n
stack = [n]
for i in range(n-1, -1, -1):
    while len(stack)> 1 and maxHeights[stack[-1]] >= maxHeights[i]:
        stack.pop()
    j = stack[-1]
    right[i] = (j-i) * maxHeights[i] + (right[j] if j < n else 0)
    stack.append(i)
```

最後就是找出global maximum

```py
res = 0
for i, peak in enumerate(maxHeights):
    res = max(res, left[i]+right[i]-peak)
return res
```