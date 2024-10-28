# Intuition

## Brute Force

兩個迴圈, 遍歷要移除的index, 然後再以O(n)計算gcd, lcm

```py
res = 0
for removeIdx in range(-1, n):
    GCD, LCM = 0, 1
    for i in range(n):
        if i == removeIdx: continue
        GCD = gcd(GCD, nums[i])
        LCM = lcm(LCM, nums[i])
    
    res = max(res, GCD*LCM)
```

## Time Complexity Optimization

我們可以先預處理求出:
- prefixGCD[i], suffixGCD[i]
- prefixLCM[i], suffixLCM[i]

那這樣對於當前移除index `i`, 其GCD, LCM分別為`gcd(prefixGCD[i-1], suffixGCD[i+1])`跟`lcm(prefixLCM[i-1], suffixLCM[i+1])`


首先預處理:

```py
n = len(nums)

preGCD = [0]
preLCM = [1]
for i in range(n):
    preGCD.append(gcd(preGCD[-1], nums[i]))
    preLCM.append(lcm(preLCM[-1], nums[i]))

sufGCD = [0] * (n+1)
sufLCM = [1] * (n+1)
for i in range(n-1, -1, -1):
    sufGCD[i] = gcd(sufGCD[i+1], nums[i])
    sufLCM[i] = lcm(sufLCM[i+1], nums[i])
```

那再來就遍歷`removeIndex`以及沒有移除任何index情況, 求出全局最佳即可
對於`removeIndex`來說, 移除後的GCD, LCM分別為:

```py
res = preGCD[-1] * preLCM[-1]

for removeIndex in range(n):
    GCD = gcd(preGCD[removeIndex], sufGCD[removeIndex+1])
    LCM = lcm(preLCM[removeIndex], sufLCM[removeIndex+1])
    res = max(res, GCD*LCM)
return res
```