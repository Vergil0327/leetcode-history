# Intuition

如果n=3的話:
aba, abc, bca, ...

可以想成我們有這三個排序過個字母可用`["a", "b", "c"]`
我們如果用preorder traversal DFS的話, 便會得到以字典序排序而構建出來的字串
再加上題目所述的條件
前後當前字母不可與前一個字母相同, 並且長度必須為`n`這兩個條件後
再用個global variable `self.count`來紀錄當前構造的是第幾個字串, 等到我們構建到第`k`個後
我們直接紀錄答案並直接終止DFS即可

# Other Solution

除了首字母外, 後續都只有兩種可能

```py
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # a X X X X X: 2**(n-1) possible happy string
        # b X X X X X: 2**(n-1) possible happy string
        # c X X X X X: 2**(n-1) possible happy string
        if k > 3 * 2**(n-1): return ""
        
        self.res = []
        def dfs(m, k):
            if m == 0: return
            skip = k // 2 ** (m-1) # 從"a"開始往後跳過幾輪. skip=0 -> a; skip=1 -> b; skip=2 -> c
            ch = chr(ord("a") + skip)

            if self.res and ch >= self.res[-1]: # 前一個字母是a, 當前也是b的話, 還得再跳過一輪, 因為前面計算是從"a"開始, 但前一個字母"b"的下一個字母不可以也是"b", 所以跳過的b, 因此這輪應該是c
                ch = chr(ord(ch)+1)

            self.res.append(ch)
            dfs(m-1, k - skip * 2**(m-1))

        dfs(n, k-1)
        return "".join(self.res)
```