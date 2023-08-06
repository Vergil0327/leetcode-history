# Intuition

`the elegance of a subsequence of items = total_profit + pow(distinct_categories2, 2)`

直覺想到的是:
- 可選可不選 take or skip, 直到size == k
- 優先選profit高的 => sort items by profit in decreasing order
- 紀錄distinct categories
=> 但這樣遍歷搜尋下去會 TLE (1 <= items.length == n <= 10^5)

所以換個思路
首先先排序, 然後我們取前k個items => 這樣我們會得到最大的total_profit
=> 由於`elegance = total_profit + pow(distinct_categories2, 2)`
=> 代表我們在items[k:]內的所有候選, 任一選來替換都只會減少total_profit而不會增加
=> 代表我們想要從items[k:]裡面選的item, 必須是distinct item, 這樣才會增加`pow(distinct_categories2, 2)`這項

那既然我們知道從items[k:]內挑選的條件了, 那麼對於目前選的前k個items, 我們應該換掉哪個才對?
1. 首先直覺想到的肯定是拿profit最小的一個
2. 最好還是non-distinct item
    => 這時再想一下, 如果要替換的種類數目只有一個, 這時如果替換掉他, 除了total_profit肯定變小外, 替換之後的distinct數目也還是不變
    => 代表我們其實不可以挑選distinct item

因此綜合上面分析, 如果我們要從前k個裡選任意一個item移除必須符合以下兩個條件:
1. profit最小
2. 該種類數目必須>1
如果任一不符合, 那替換後的結果肯定比選前k個item來得小

所以我們必須紀錄每個種類的duplicate, 然後從中依次選小的來跟後面candidate來替換
並盡量藉由將每個duplicate都換成distinct item來增加`pow(distinct_categories2, 2)`這項

最後我們取全局最大`res = max(res, total_profit + pow(distinct_categories2, 2))`
直到用光所有duplicate, 此時`pow(distinct_categories2, 2)`這項就會最高

