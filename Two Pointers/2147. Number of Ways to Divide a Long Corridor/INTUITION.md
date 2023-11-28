# Intuition

count plants in between every two seats

*note. leading and trailing plants contribute nothing*

```
SS[PPPP]SPS
res = 1 * (# of P + 1) % (10^9+7)
```

edge case: seats must be `even` or we can't have valid nonoverlapping section

# Intuition 2

其實我們只需關注seats的位置即可

找出seats的index後, 兩兩找出相對應index
```py
seats = [i for i,c in enumerate(corridor) if c == 'S']

res = 1
mod = 10**9+7
for i in range(1,len(seats) - 1,2):
    res *= seats[i+1] - seats[i]
    res %= mod
```

最後再查看結果有沒有滿足以下條件即可:
1. len(seats)%2 == 0
2. len(seats) >= 2
