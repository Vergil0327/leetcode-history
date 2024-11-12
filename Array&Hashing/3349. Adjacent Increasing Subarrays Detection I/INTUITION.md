# Intuition

直覺想到的是紀錄max_length[i]: the maximum length of the strictly increasing subarray ending at index i

```py
n = len(nums)
max_length = [0] * (n+1)
for i in range(n):
    if nums[i] > nums[i-1]:
        max_length[i+1] = max_length[i] + 1
    else:
        max_length[i+1] = 1
```

有了這項資訊後, 我們就能判斷:

1. 如果max_length[i] >= 2*k, 那麼肯定能拆成兩段長度為`k`的strictly increasing subarray
2. 如果max_length[i]位置跟max_length[i-k]這兩個位置都是都是長度`>=k`的strictly increasing array


```py
for length in max_length:
    if length >= 2*k: return True

for i in range(1, n+1):
    if i-k < 0: continue
    if max_length[i] >=k and max_length[i-k] >= k:
        return True
return False
```