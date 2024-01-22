# Intuition

**求最短路徑 => try BFS**

但還有另一個dp解法:

# Intuition 2
 
等比級數和: a1 * (1-r^n) / (1-r)
所以 => distance = (1-2^n) / (1-2) = 2^n-1

那我們抵達target有兩種可能:
1. distance <= target, 往前抵達
2. distance > target, 回頭抵達

### 第一種情況

在`distance <= target`之前抵達, 我們可以選擇要不要煞車回頭然後再往前
ex. target=4 => A A R R A => answer=5

所以`distance = pow(2, n)-1 <= target`時 => n <= log2(target+1)
也就是在`n <= log2(target+1)`時, 我們可以選擇回頭幾步後在往前, 由於不知道要幾步, 我們就都遍歷一下

```py
op2_cost = 1
for k in range(n): # back step
    dp[target] = n + op2_cost + k + op2_cost + self.racecar(target - distance(n) + distance(k))
```

### 第二種情況

那如果是在`distance > target`後再回頭抵達的話,
回頭時速度從-1開始, 所以其實只是方向相反而已, 所以不管方向的話,
超過target就等於是從距離終點target的(distance-target)位置再往前要抵達到target的意思,
而這時照理說dp[distance-target]應該已經在之前就已經求過, 所以:

```py
op2_cost = 1
dp[target] = (n+1) + op2_cost + self.racecar(distance(n+1)-target)
```
