# Intuition

加入nums[i]後三種情況:

```
X X X Left nums[i]

nums[i] Right X X X

X X X Left nums[i] Right X X X
```

如果nums[j]加入後是在頭或尾:
    - 如果nums[i]-1==Left or nums[i]+1==Right任一成立, 整體imbalance不變
    - 如果nums[i]-1 != Left and nums[i]+1 != Right, 整體imbalance += 1

如果left < Right-1: imbalance = 1
    - 加入nums[i]後, 如果nums[i]-1 == Left and nums[i]+1 == Right => 原本[Left,Right]的imbalance沒了, 整體imbalance -= 1
    - 如果nums[i]-1==Left or nums[i]+1==Right任一成立, 整體imbalance不變
    - 如果nums[i]-1 != Left and nums[i]+1 != Right, 整體imbalance += 1

# Complexity

time: $O(n^2)$

space: $O(n)$