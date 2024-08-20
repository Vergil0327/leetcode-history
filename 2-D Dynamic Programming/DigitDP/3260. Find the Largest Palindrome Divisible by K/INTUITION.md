# Intuition

這題真的是毫無想法, 有想到digit dp
但想不到該如何應用**k divisible**進去來避免TLE, 直到看到[Digit DP solution by @awice](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/solutions/5653838/python-digit-dp/)

首先digit DP的大體框架為:

```py
res = [9] * n

@cache
def dfs(i):
    if i == (n+1)//2: # base case

    for d in range(9, -1, -1):
        res[i] = res[~i] = d
        dfs(i+1)

dfs(0)
return "".join(map(str, res))
```

我們需要**exactly** n-size的palindrome string, 並且值要最大
所以一開始可以先假定初始值為`[9]*n`

再來由於是palindrome, 所以每次digit都是同步更新`res[i] = res[~i] = digit for digit in range(9, -1, -1)`
遞歸去組出digit並且greedily由大到小嘗試擺放digit到res裡

有了這框架後, 再來就是最關鍵的一步: **如何在建構palindrome的過程去判斷是否能被k給整除**
判斷是否整除我們只需看最後除以k的餘數是不是為0, 所以我們肯定要有個狀態去紀錄

我們額外用`remainder`去儲存當下的餘數, 那麼餘數的狀態轉移則為:

`new_remainder = (remainder * 10 + {res[i]跟res[~i]這兩個位置的餘數})%k`
- 假設這兩個位置放入的digit為`d`, 那麼這兩個位置的餘數為
- res[i]: d * pow(10, i)
- res[~i] = res[n-1-i]: d * pow(10, n-1-i)

```
所以new_remainder = (current_remainder + d * pow(10, i) + d * pow(10, n-1-i)) % k
                  = (current_remainder + d * pow(10, i) + d * pow(10, n-1-i)) % k
                  = current_remainder % k + d * pow(10, i) % k + d * pow(10, n-1-i) % k
                  = current_remainder % k + d * (pow(10, i) % k + pow(10, n-1-i) % k)
                  = current_remainder % k + d * coeff
```
而這個`pow(10, i) % k`跟`pow(10, n-1-i) % k`都是可以預先計算好的

```py
# pow10 mod k
kmod = [1] * n
for power in range(1, n):
    kmod[i] = kmod[i-1]*10%k
```

因此整體digit DP為:

```py
res = [9] * n

@cache
def dfs(i, remainder):
    if i == (n+1)//2: # base case
        return remainder == 0

    for d in range(9, -1, -1):
        res[i] = res[~i] = d
        
        # 我們會一路擺放digit到中央位置, 所以i跟n-1-i有可能是同個位置
        # 為了避免重複計算, 這寫法更簡潔 => coeff = sum(kmod[j] for j in {i, n-1-i})
        coeff = kmod[i] + kmod[n-1-i] if n-1-i != i else kmod[i]

        new_remainder = (remainder + coeff * d)%k # remainder的狀態轉移
        if dfs(i+1, new_remainder): return True
    return False

dfs(0, 0)
return "".join(map(str, res))
```

由於我們digit由大到小擺放, 所以一但找到答案, 肯定是最佳解, 我們就退出遞歸

time: $O(k * (n+1)//2 * 10)$
space: $O(k*n)$

# Pure Math Solution

數學解就不多作介紹, 無實際參考價值
基本上是根據[divisibility rules](https://en.wikipedia.org/wiki/Divisibility_rule)去case by case的寫出對應

```py
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1:
            return '9' * n
        elif k == 2:
            if n <= 2:
                return '8' * n
            else:
                return '8' + '9' * (n - 2) + '8'
        elif k == 3 or k == 9:
            return '9' * n
        elif k == 4:
            if n <= 4:
                return '8' * n
            else:
                return '88' + '9' * (n - 4) + '88'
        elif k == 5:
            if n <= 2:
                return '5' * n
            else:
                return '5' + '9' * (n - 2) + '5'
        elif k == 6:
            if n <= 2:
                return '6' * n
            elif n % 2 == 1:
                l = n // 2 - 1
                return '8' + '9' * l + '8' + '9' * l + '8'
            else:
                l = n // 2 - 2
                return '8' + '9' * l + '77' + '9' * l + '8'
        elif k == 8:
            if n <= 6:
                return '8' * n
            else:
                return '888' + '9' * (n - 6) + '888'
        else:
            dic = {0: '', 1: '7', 2: '77', 3: '959', 4: '9779', 5: '99799', 6: '999999', 7: '9994999',
                       8: '99944999', 9: '999969999', 10: '9999449999', 11: '99999499999'}
            l, r = divmod(n, 12)
            return '999999' * l + dic[r] + '999999' * l
```