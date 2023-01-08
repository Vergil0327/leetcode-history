"""
數位計算

我們計算對於每個 `i` 位如果是1的話, 有多少個組合符合

n = 23145
s = 2 3 1 4 5
    Y Y i X X

例如i為百位且是"1"的可能性有:
第i位左邊首先計算 00 ~ 22 = 23145 // 100 = 23種可能
第i位右邊首先計算 00 ~ 99 = 10 ** 2 = 100種可能
因此目前為止總共有: 23 * 100 個1

然後再計算第i位左邊為 23 的情況: "23 i XX"
1. 如果原本的`n`,第i位 > 1, 那麼也就是 231XX 的右邊這兩位XX就可以是 00 ~ 99
   所以可以再多100個1
2. 如果原本的`n`,第i位 = 1, 那麼也就是 231XX 的右邊兩位XX僅有 00 ~ 原本n的後兩位數可能
   所以可以再多 n%100+1 (+1是因為00也算, 00~45有45+1個選擇)
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        #                n = 23145
        #                s = 2 3 1 4 5
        #                    Y Y i X X
        # digits(1-index) -> 5 4 3 2 1
        s = str(n)
        digits = len(s)
        
        cnt = 0
        for i in range(1, digits+1):
            left = n // 10**i
            cnt += left * 10**(i-1)

            if int(s[digits-i]) > 1:
                cnt += 10 ** (i-1) # i digits: 00...00 ~ 99...99
            elif int(s[digits-i]) == 1:
                cnt += n % 10**(i-1) + 1 # 00...00 ~ s[i:] + 1. ex. 00 ~ 12 is 13 choices
            # elif int(s[digits-i]) == 0:
            #     current digit can't attribute any "1"
        return cnt