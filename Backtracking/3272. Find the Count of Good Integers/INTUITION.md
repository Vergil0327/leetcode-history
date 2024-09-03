# Intuition

首先想到digit dp找k-palindromic integer的方法
由於要組出palindromic integer, 我們只需要組出左半邊(含中心即可)
所以只需要組出`(n+1)//2`長度的string, 並在過程中持續記錄當前的remainder

"{XYZ}YX", n=5
i=0, X => k-remainder += (X*pow(10, i) + X * pow(10, n-i-1))%k
i=1, Y => k-remainder += (Y*pow(10, i) + Y * pow(10, n-i-1))%k
i=2, Z => k-remainder += (Y*pow(10, i)) => center

當n為奇數時, 會有中心存在, 得注意避免重複計算
框架會像是這樣

```py
m = (n+1)//2

@cache
def dfs(i, num):
    if i == m:
        return (num%k) == 0

    center = 0 if n%2==1 and i == m-1 else 1
    res = 0
    for d in range(10):
        if i == 0 and d == 0: continue # no leading zeros
        cur = d*pow(10, i) + d*pow(10, n-i-1)*center
        res += dfs(i+1, num + cur)
    return res
return dfs(0, 0)
```

但這題是要找出所有可以透過重新排列而組成k-palindromic的數

brute force的話就直接backtracking然後全丟到set裡看有多少個

```py
m = (n+1)//2

self.SET = set()
def dfs(i, num):
    if i == m:
        if num in self.SET: return
        if num%k == 0:
            arr = list(map(int, list(str(num))))
            SET = set()
            for perm in permutations(arr):
                if perm[0] == 0: continue
                self.SET.add(perm)
            return

        
        return

    center = 0 if n%2==1 and i == m-1 else 1

    for d in range(10):
        if i == 0 and d == 0: continue # no leading zeros
        cur = d*pow(10, i) + d*pow(10, n-i-1)*center
        dfs(i+1, (num + cur))
    return

dfs(0, 0)
return len(self.SET)
```

但這樣會TLE (60 / 90 testcases passed), 過程中有太多重複計算

最後是參考[這篇的計算 by @donpaul299](https://leetcode.com/problems/find-the-count-of-good-integers/solutions/5716103/brute-force/)

框架不變, 主要補足計算以及去除重複permutations的方法

概念是每當我們找到合法的k-palindromic
我們計算他的所有permutations數目: `factorial(n) // (factorial(duplicate_digit) * ...)`

並同時將當前的k-palindromic的footprint加入到hashset `visited`裡來避免重複

但由於leading zero是不合法的, 所以我們得再檢驗一下
假如我們有用到"0", 也就是digits[0] > 0, 我們必須把所有leading zero的permutation給扣掉



```py
self.visited = set()
def count(num):
    s = str(num)
    n = len(s)
    if n == 1: return 1

    digits = [0] * 10
    for i in range(n):
        digits[int(s[i])] += 1
    
    # calculate # of permutations
    tot = factorial(n)
    for i in range(len(digits)):
        cur = digits[i]
        if cur != 0:
            tot //= factorial(cur) # remove duplicate permutations

    # add footprint into hashset to avoid duplicate calculation
    key = tuple(digits)
    if key in self.visited: return 0
    self.visited.add(key)

    if digits[0] == 0: return tot

    # 扣掉permutations with leading zero
    leading_0_perm = factorial(n-1)
    leading_0_perm //= factorial(digits[0]-1)

    for i in range(1, len(digits)):
        cur = digits[i]
        if cur != 0:
            leading_0_perm //= factorial(cur)
    return tot-leading_0_perm
```