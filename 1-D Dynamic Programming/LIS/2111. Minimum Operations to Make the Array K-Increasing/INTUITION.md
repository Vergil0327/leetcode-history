# Intuition

k-increasing means:
arr[i] <= arr[i+k] for i in range(n-k),

also means:
arr[i] <= arr[i+k] <= arr[i+2k] <= ...
arr[i+1] <= arr[i+1+k] <= arr[i+1+2k] <= ...

所以我們可以用`i%k`來分出每一串數字:
`nums where nums = [arr[i], arr[i+k], ...] where 0 <= i < k`

那麼每一串數字如果我們求出length of longest increasing subsequence = m
最低操作數就是`len(nums) - m`
最後全部的最低操作相加即為答案