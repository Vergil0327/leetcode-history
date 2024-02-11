# Intuition

突然想到我們可以先把nums換成pattern的形式
```py
for i in range(n-1):
    if nums[i+1] > nums[i]:
        nums[i] = 1
    elif nums[i+1] < nums[i]:
        nums[i] = -1
    else:
        nums[i] = 0
```
那再來問題就類似在string中找有多少個pattern substring存在
從數據規模來看, 要O(n)時間複雜度的話看來是要用 KMP 

由於KMP是string的演算法, 我們先把`1`, `-1`, `0`分別用abc表示好了
那後面就是套KMP模板找出target substring即可