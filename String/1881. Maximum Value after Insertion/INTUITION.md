# Intuition

正數就想辦法讓digits part為最大值
反之如果是負數, 就想辦法讓digits part為最小值

那再來就是找出插入的index即可

- 正數: 找出第一個小於`x`的digit in `n`
- 負數: 找出第一個大於`x`的digit in `n`

# Complexity

time: O(n)
space: O(1)