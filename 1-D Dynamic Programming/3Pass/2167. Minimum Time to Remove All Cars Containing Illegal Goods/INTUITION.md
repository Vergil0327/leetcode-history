# Intuition

直覺想到的是找出分界點然後:
- 從左往右找出只用**op.1**或**op.3**找出截至i-th element為止的最小cost
- 再從右往左找出只用**op.2**或**op.3**找出截至i-th element為止的最小cost

所以定義:
left_cost[i]: the minimum operations considering s[0:i] (both inclusive)
right_cost[i]: the minimum operations considering s[i:n-1] (both inclusive)

狀態轉移就是

1. 利用op.1: left_cost[i] = i+1 (0-indexed, 從左到右整個長度)
2. 利用op.3: left_cost[i] = left_cost[i-1] + 2
上述兩者取小就是left_cost[i]

同理right_cost[i]就是由右往左更新
1. 利用op.1: right_cost[i] = n-i (0-indexed, 從右到左整個長度)
2. 利用op.3: right_cost[i] = right_cost[i+1] + 2

再來我們就遍歷分界點取全局最小即可: min(left_cost[i]+right_cost[i+1])