# Intuition

這題其實紀錄prefix sum以及prefix digits並同時紀錄digits size後, 即可O(1)時間計算出我們要的`digits * digits_sum % mod`

```py
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 1_000_000_007
        n = len(s)

        digits = [0]
        digitsum = [0]
        digit_size = [0]

        pow10 = [1]
        for i in range(1, n+1):
            pow10.append(pow(10,i,mod))

        for i in range(n):
            d = int(s[i])
            if d == 0:
                digits.append(digits[-1])
                digit_size.append(digit_size[-1])
            else:
                digits.append(digits[-1]*10 + d)
                digit_size.append(digit_size[-1]+1)

            digitsum.append((digitsum[-1] + d) % mod)

        res = []
        for l, r in queries:
            # x = digits[r+1] - digits[l] * pow(10, digit_size[r+1]-digit_size[l], mod)
            x = digits[r+1] - digits[l] * pow10[digit_size[r+1]-digit_size[l]]
            y = digitsum[r+1] - digitsum[l]

            res.append(x * y % mod)

        return res
```

但結果卻卡在MLE (memory limit exceeded)
看了解答才想到, 我們可以用`length`為key, 而非使用index `i`
那這樣就能避免在`0` digit位置也因為prefix的特性而存上許多數值