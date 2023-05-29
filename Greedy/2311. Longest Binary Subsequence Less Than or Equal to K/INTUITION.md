# Intuition

很顯然的, 直覺想到的的top-down dp 會是 O(1000 * 10^9)
顯然是超時的

Brute Force Solution
```py
class Solution_TLE:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        
        memo = [defaultdict(lambda: -1) for _ in range(n)]
        def dfs(i, binary):
            if i == n: return 0

            if memo[i][binary] != -1:
                return memo[i][binary]

            # pick or skip
            memo[i][binary] = dfs(i+1, binary)
            if (v := (binary<<1)+int(s[i])) <= k:
                memo[i][binary] = max(memo[i][binary], dfs(i+1, v) + 1)

            return memo[i][binary]

        return dfs(0, 0)
```

這時就要思考有沒有什麼比較好的策略

對於一個binary string來說, 我們要讓值`binary string <= k`最好的方法肯定是移除高位的1
一但想到這個, 那整個就豁然開朗了

首先我們先想一下如何比較binary string的大小
我們先把k同樣轉為binary string來看的話

如果當前`s`跟`k`為:
```
s = 1110110000111101011000101
k =  101100101011101100110100
```

由於這題允許leading zeros, 所以每個leading zeros都是可以保留的, 並且是越多越好
所以其實我們需要的, 就只是從高位遍歷到低位, 並且每當`s[i] == 1`時我們就查看一下
`s[i] == 1`時才是我們關注的, leading zeros都是不必刪除的

假如一開始的s就小於k的話, len(s)就是我們的答案
很簡單可以想到我們的答案`res`的最大值為`len(s)`

再來如果當`s[i] == 1`時, 我們就分幾個case來討論:
1. 如果這時`len(s[i:])>k`:
   - 很顯然的這時s[i:]的值必定大於k, 我們就刪除當前這個高位的`1`
   - 因此`res -= 1 where res = len(s) initially`

2. 如果這時`len(s[i:]) == k`:
   - 由於位數相等, 我們直接比較兩者值大小即可
     - 對於相同位數的狀況來說, 不管是二進位來看或是十進位來看都一樣
     - ex. 101 > 100
   - 如果 `int(s[i:]) > int(binary_string(k))`, 那麼一樣`res -= 1`
   - 反之如果這時`int(s[i:]) <= int(binary_string(k))`, 那麼res就是答案

3. 如果`len(s[i:]) < k`:
   - 那麼這時二進位值肯定小k, 直接返回`res`

因此這麼分情況討論後
其實就會得出這個Greedy solution