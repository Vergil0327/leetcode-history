# Intuition

一開始想法是:
in order to find digit string within [left, right] => 首先想到digit DP, 利用digit dp 可以組出所有在這範圍內的digit string

再來就判斷當前組的digit string是不是palindrome, 如果是再判斷是不是super-palindrome

所以本體框架會是個DFS去找出所有合法範圍的digit string:

def dfs(i, isGreaterThanLow, isLowerThanHigh, hasLeadingZero, current_integer_str): return the number of super-palindrome

那digit 模板為:

```py
# 將left (lowerbound)的length補上leading zero直到跟right (upperbound)一樣
n = len(right)
while len(left) < n:
    left = "0" + left

def dfs(i, isGreaterThanLow, isLowerThanHigh, hasLeadingZero, cur):
    start = 0 if isGreaterThanLow else int(low[i])
    end = 10 if isLowerThanHigh else int(high[i])+1
    
    res = 0
    for valid_digit in range(start, end):
        res += dfs(i+1,
                    isGreaterThanLow or valid_digit > int(low[i]),
                    isLowerThanHigh or valid_digit < int(high[i]),
                    hasLeadingZero and valid_digit == 0,
                    cur+str(d))
    return res

return dfs(0, False, False, True, "")
```

**base case**

if i == 0: return 1 if isPal(current_integer_str) and isSuper(current_integer_str) else 0

但這樣會**TLE/MLE**, ex. left = "40000000000000000", right = "50000000000000000"
所以我們得另外再想個辦法

看起來palindrome跟square number並無太大關係，所以看起來只能先找一個然後再篩選另一個
1 <= left.length, right.length <= 18 => superpalindrome最多到10^18
代表palindrome最多到 sqrt(10^18)=10^9

要找出10^9以內的square number還是很多, 比較理想應該要先找比較稀疏的palindrome然後再篩選出square number
要構造palindrome由於前後會是鏡像相等, 所以僅需要考慮一半
因此僅需要遍歷最多10^5範圍內的數即可

所以整體框架為:
僅需要再實作**constructPalindrome**即可
```py
lo, hi = int(left), int(right)
res = 0
for num in range(1, 10**5+1):
    palindrome = constructPalindrome(num)
    superPal = palindrome * palindrome
    if lo <= superPal <= hi and ispal(str(superPal)):
        res += 1
return res
```

遍歷的這個上下界[1, 10**5], 我們可以根據left跟right來更縮小一點
從superpalindrome往回推, string.length / 4 是可能的palindrome大小
所以我們:
- start = max(1, pow(10, len(left)//4-1)), 保守一點位數多少一位
- end = max(1, pow(10, len(right)//4+1)), 保守一點拉大上界, 長度多一位
