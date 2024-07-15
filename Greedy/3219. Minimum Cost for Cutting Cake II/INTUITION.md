# Intuition

直覺上可以用四個邊界(left, right, top, down)並用dfs+cache來搜索出最佳解 => see [3218. Minimum Cost for Cutting Cake I]
但這邊數據規模改為`1 <= m, n <= 10^5`, 原本方法肯定會TLE
因此再以3218為基礎上如果要再優化, 或許可以greedily去切?

每一刀肯定都要切到, 最後才能都是1x1 block
每切一刀, 一分為二
水平一刀, 該方向每一塊block都會多一塊需要垂直一刀
垂直一刀, 該方向每一塊block都會多一塊需要水平一刀

try greedy: 直覺上來想, 我們優先切cost大的, 然後再切cost小的
所以這時候順序對我們來說已不重要, 我們可以對horizontalCut跟verticalCut做排序
再來就用two pointers, i, j 分別代表pointer of horizontalCut and veticalCut
然後我們從cost大的開始切割, 也就是:

- 如果horizontalCut[i] >= verticalCut[j]: 我們選擇切horizontalCut
    - 對於當前horizontalCut[i], 我們需要切割(j+1)次
    - horizontal cost = horizontalCut[i] * (j+1) if i < len(horizontalCut) else 0
    - j+1: # of horizontal cut we need, (i.e. number of blocks in vertical direction)

- 如果horizontalCut[i] < verticalCut[j]: verticalCut
    - 對於當前verticalCut[j], 我們需要切割(i+1)次
    - vertical cost = verticalCut[j] * (i+1) if j < len(verticalCut) else 0
    - i+1: # of vertical cut we need (i.e. number of blocks in horizontal direction)