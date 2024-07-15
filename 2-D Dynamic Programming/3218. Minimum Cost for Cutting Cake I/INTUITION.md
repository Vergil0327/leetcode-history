# Intuition

我們可以用top-down dp (dfs+cache)來探索所有可能切法, 紀錄四個邊界狀態去切, 直到最後變為1x1
note. 我們horizontalCut, verticalCut都改為1-indexed來配合我們的dfs