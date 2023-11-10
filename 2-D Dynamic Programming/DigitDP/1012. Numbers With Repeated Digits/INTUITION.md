# Intuition

數值範圍[1, 10^9], 一開始想到的是如果是用digit DP的概念來找出[1,n]範圍內的所有合法digit
我們位數一位一位看的話, 最多就9位, 並且用state記錄當前digit的狀態

dight範圍0-9, 所以我們用一個長度為10的string來代表當前digit的個數狀態:
ex. "0210000000"代表1有2個, 2有1個, 其他digit都是0
同時為了方便memorization, 我們把所有重複超過2的狀態都記錄成2, 這樣最後我們只要判斷:

只要"2"存在於state裡, 就代表有超過一個digit是重複超過一次的, 那麼該digit string即為合法 => answer += 1

*note. 要注意, **leading zero**不可算在state裡*

# Other Solution (more efficient)

X: 1-9
XX: 10-99 => {11,22,33,44,55,66,77,88,99}
XXX: 100-999 => {...}

我們可以反過來想, 總共n個數我們減去所有distinct digit(不重複的digit)後, 剩下的就是我們要的答案

那該如何找distinct digit的個數?

當length = 3, num = X X X
每位數都不重複的num總共有這麼多個: **P(10, length) - P(9, length-1)**

P為permutation, 代表0-9共十個數字中挑出length位來, 但由於首位數不可以是0, 不然就不是length位數了
所以再扣掉首位為**0**的permutation個數: P(9, length-1)
因此3位數數字中, 每位數都是distinct的個數為**P(10, length) - P(9, length-1)**

所以如果n=2345
那麼一位數,二位數,三位數的個數都可用**P(10, length) - P(9, length-1)**計算出來
但四位數就必須判斷數值有沒有超過n了

所以四位數我們逐位看:

第一位數:
0 => 首位數不可以為leading zero, skip
1 => 首位為1, 那麼後面位數就可以任選, 所以個數為 {0,2,3,4,5,6,7,8,9} 這些digit中挑出3個
2 => 首位為2, 那麼就遞歸再看下個位數可以是多少:
    => 2[_]XX:
    => 0: 剩餘可用的digits裡挑出2個來. (剩兩個XX)
    => 1: 剩餘可用的digits裡挑出2個來. (剩兩個XX)
    => 2: 剩餘可用的digits裡挑出2個來. (剩兩個XX)
    => 3: 再往下看下個位數 =>會發現是個遞歸

```py
def P(m, n):
    res = 1
    for i in range(n):
        res *= (m-i)
    return res
    
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        m = len(s)

        self.res = 0
        # 先計算1到m-1位數的no_repeat num
        for length in range(1, m):
            self.res += P(10, length) - P(9, length-1)

        def count_no_repeat(i, visited):
            if i >= m: # 代表組出m位數並且沒有任何repeat的num
                self.res += 1
                return

            for d in range(10):
                if i == 0 and d == 0: continue # leading zero
                if visited[d]: continue
                if d < int(s[i]):
                    # 0-9共十個digit, 用去i+1個, 所以從剩下的10-(i+1)的digit裡分配到後面的m-(i+1)位
                    self.res += P(10-(i+1), m-(i+1))
                elif d == int(s[i]):
                    visited[d] = 1
                    count_no_repeat(i+1, visited)
                    visited[d] = 0

        count_no_repeat(0, [0]*10)
        return n-self.res
```