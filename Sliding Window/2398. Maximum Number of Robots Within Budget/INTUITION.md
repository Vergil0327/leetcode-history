# Intuition

first, think brute force

```
X X X [X X X]
       j   i
```

```py
robots = 0
for i in range(n):
    for j in range(i, -1, -1):
        cost = max(chargeTimes[j:i]) + (i-j+1) * sum(runningCosts[j:i])
        if cost <= budget:
            robots = max(robots, i-j+1)
```

maybe we can try sliding window and maintain its cost <= budget

1. sum(runningCosts[j:i]) -> prefix sum -> we don't need it. we can just maintain sliding window sum
2. max(chargeTimes[j:i]) -> maxHeap

time: O(nlogn)