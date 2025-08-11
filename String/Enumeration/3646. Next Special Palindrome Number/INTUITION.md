# Intuition

> A number is called special if:
>   - It is a palindrome.
>   - Every digit k in the number appears exactly k times.

所以我們能用來組成palindrome的digits有: `1`, `22`, `333`, `4444`, `55555`, `666666`, `7777777`, `88888888`, `999999999`
首先很明顯能看到, 如果使用到奇數長度的digits, 只能選擇一個使用, 不然無法形成palindrome

所以先試著brute force看看, 產生所有可能的palindrome:

```py
from itertools import permutations
class Solution:
    def specialPalindrome(self, n: int) -> int:
        odd = ['', '1', '3', '5', '7', '9']
        even = ['2', '4', '6', '8']
        states = 1<<len(even)

        res = float('inf')
        for mid in odd:
            digits = []
            if mid and int(mid) > 1:
                for _ in range(int(mid)//2):
                    digits.append(mid)

            for state in range(states):
                left = digits.copy()
                for i in range(len(even)):
                    if (state>>i)&1:
                        left += [even[i]] * (int(even[i])//2)
                if not mid and not left: continue

                length = len(left)*2 + (0 if not mid else 1)
                if length < len(str(n)): continue # generated palindrome can't be greater than n
                
                for perm in permutations(left, len(left)):
                    s = "".join(perm)
                    candidate = int(s + mid + s[::-1])
                    if candidate > n:
                        res = min(res, candidate)
        return res
```

但發現這樣太慢, 但仔細想想, 我們要找一個剛好大於n的數, 那麼不管n是奇數長度或偶數長度
最終答案至多只會比str(n)的長度再多一位, 所以我們再加個條件

`if length > len(str(n)) + 1: continue`, 近一步排除掉太大的palindrome

如此一來, 就過了
這題其實可能的palindrome沒有多少種, 全部找出來然後找出剛好大於n的即可

# Time Complexity

time = mid enumeration * even number chosen state * permutations
     = 6 * 2^4 * 8! = 3870720
     -> 約10^6級別 -> OK for leetcode

至於為什麼permutatino上限是`8!`是因為`n <= 10^15`
代表我們最多只會組出長度為16的palindrome, 那麼一半長度的permutation為`8!`