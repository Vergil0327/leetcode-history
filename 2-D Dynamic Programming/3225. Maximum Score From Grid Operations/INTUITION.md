# Intuition

對於當前col來說, 我們可以塗黑[0, h] where h < n這段範圍
有點像是在grid上面從top row開始往下畫histogram

為了求最高分數, 首先想到的是dynamic programming
觀察一下, 我們看當前col的話, 能否得分數的關鍵跟`col-1`以及`col+1`有關
當兩者任意塗黑時, 當前col就能得分

所以對於當前`col`來說, 我們需要知道`col-1`跟`col+1`的height

所以我們狀態必須紀錄:

1. 當前處理到第幾個col
2. col-1的塗黑高度
3. col-2的塗黑高度

然後開始討論三個col的可能情況

當前為`col`, 遍歷當前塗黑高度`h`, preHei為`col-1`的塗黑高度, prePreHei為`col-2`的塗黑高度:

1. **preHei >= h**: 當前`col`能得分`col_presum[col][preHei] - col_presum[col][h]`
2. **preHei < h**: 當前col沒有得分, 再來考慮當前`col`塗黑高度`h`對`col-1`的影響
    1. ** (preHei < h and) preHei < prePreHei**: 對於`col-1`來說會是個凹下去的形狀
        - 這邊不計算, 因為這邊有兩種情況, 可能`col`高度大於`col-2`也可能`col`高度小於`col-2`
        - 在`col`小於等於`col-2`的情況已經在第一點計算
        - 在`col`大於`col-2`的情況, 我們統一在下一步計算
        - 這樣才能避免重複計算
    2. ** PrePreHei <= preHei < h**: `col-2` -> `col-1` -> `col`會是個塗黑高度遞增的形狀, 補上當前`col`對`col-1`的影響

```py
res = 0
for h in range(n + 1):
    if preHei >= h:
        curScoreFromLeft = col_presum[col][preHei] - col_presum[col][h]
        res = max(res, dfs(col + 1, h, preHei) + curScoreFromLeft)
    elif prePreHei > preHei:  # prePreHei > preHei and preHei < h => 凹形 => already calculated above at previous round
        res = max(res, dfs(col + 1, h, preHei))
    else:  # 此時 prePreHei <= preHei < h, 代表高度遞增 => 對於col-1來說, 必須補上col高出col-1那段高度差的得分
        prevScoreFromRight = col_presum[col - 1][h] - col_presum[col - 1][preHei]
        res = max(res, dfs(col + 1, h, preHei) + prevScoreFromRight)
```


可惜這樣時間複雜度會是O(n^4) => **TLE**

再來這步優化, 不太好想
直到看到這篇[【图解】DP 及其优化：从 n^4 到 n^3 到 n^2(Python/Java/C++/Go)灵茶山艾府](https://leetcode.cn/problems/maximum-score-from-grid-operations/solutions/2852362/tu-jie-dp-ji-qi-you-hua-by-endlesscheng-pco6)

能優化的部分是我們實際上並不需要知道prePreHei的實際高度, 其實我們只要知道prePreHei跟preHei之間的高度關係而已
所以我們可以用個boolean值來表示即可

```py
def dfs(col: int, preHei: int, isPreHeiDec: bool) -> int:
    if col >= n: return 0

    res = 0
    for h in range(n + 1):
        if preHei == h:
            res = max(res, dfs(col + 1, h, False))
        if preHei > h:
            curScoreFromLeft = col_presum[col][preHei] - col_presum[col][h]
            res = max(res, dfs(col + 1, h, True) + curScoreFromLeft)
        elif isPreHeiDec:  # preHei already < h and also preHei < prePreHei => 凹形 => already calculated above at previous round
            res = max(res, dfs(col + 1, h, False))
        else:  # 此時h > preHei, 代表高度遞增 => 對於col-1來說, 必須補上col高出col-1那段高度差的得分
            prevScoreFromRight = col_presum[col - 1][h] - col_presum[col - 1][preHei]
            res = max(res, dfs(col + 1, h, False) + prevScoreFromRight)
    return res

answer = max(dfs(1, h, False) for h in range(n + 1))
```