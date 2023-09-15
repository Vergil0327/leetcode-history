# Intuition

對於i-th person, 他能看到最遠的極限是j = nextGreater[i]
他能看到的就是在[i:j]這區間的longest increasing subsequence(LIS)都能看到
而nextGreater可以用monotonically increasing stack求得

比較直覺能想到的是透過**monotonically increasing stack**:

對於heights[stack[-1]] <= heights[i]來說, stack.pop()-th person能看的只有當前i-th person
所以:
```py
while stack and heights[stack[-1]] <= heights[i]:
    res[stack.pop()] += 1
```

當初沒注意到的是
對於stack裡的來說, 由於是單調遞增的, 所以當前的i-th person可以被stack[-1]-th person看到
所以:
```py
if stack:
    res[stack[-1]] += 1
```

另外我們也可以從後往前維護單調遞增的stack

比他矮的都看得到, 並且這些對於下個元素來說也都會被i-th person擋住, 所以可以pop掉
```py
while stack and heights[stack[-1]] <= heights[i]:
    cnt += 1
    stack.pop()
```
等到全pop完後, 如果stack還有元素, 這個就是他的i-th person的next greater,
也就是所能看到的最後一個 => `cnt += 1`

```py    
res = [0] * n
stack = []
for i in range(n-1, -1, -1):
    cnt = 0
    while stack and heights[stack[-1]] <= heights[i]:
        cnt += 1
        stack.pop()
    if stack:
        cnt += 1

    res[i] = cnt
    stack.append(i)
```

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$