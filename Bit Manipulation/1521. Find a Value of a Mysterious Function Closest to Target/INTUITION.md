# Intuition

brute force:

dp[i]: the minimum possible value of abs(func(arr, j, i)-target) for j in range(i)

也就是說:我們往回移動j找出best(AND(j, i))
```
X X X X {X X X X} X
      <- j     i
```

那麼dp[i] = best(AND(j, i) for j in range(i))
下個dp[i+1]由於AND operation的性質, 結果就相當於:
best(AND(j, i+1) for j in range(i+1)) = best(arr[i+1] & AND(j, i) for j in range(i))

dp[i] = choose best of {arr[0:i], arr[1:i], arr[2:i], ..., arr[i-1:i]}
dp[i+1] = choose best of {arr[0:i+1], arr[1:i+1], ..., arr[i:i+1]} = choose best from {arr[i+1] & all possible best value from dp[i]}

而AND是會越遠越少, 所以我們可能的數最多就32種, 越AND只會在各個bit位上產生更多0, 所以實際上在遍歷dp[i]集合時可能的數並不多
每次集合裡的數最多就32而已, 所以效率很好, 整體時間複雜度就$O(32n)$

所以我們可以用當前的arr[i]與之前的所有AND operation value進行AND operation後
更新成新的集合, 並持續更新global minimum possible value of `|func(arr, l, r) - target|`


time complexity: $O(32n)$