# # Intuition

count plants in between every two seats

*note. leading and trailing plants contribute nothing*

```
SS[PPPP]SPS
res = 1 * (# of P + 1) % (10^9+7)
```

edge case: seats must be `even` or we can't have valid nonoverlapping section
