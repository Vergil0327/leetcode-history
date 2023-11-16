# Intuition

想成俄羅斯方塊, 我們從左到右擺放
並且方塊大小由大到小使用, 盡可能減少方塊使用
但從example 3可看出並不一定就是最大的方塊能得最佳解, 所以方塊由大到小遍歷一遍進行backtracking

所以首先一開始每個位置`i`所堆積的單位方塊高度為heights[i]
由左到右陸續堆疊, 擺完一個後再找出當前高度最低的最靠左位置開始繼續堆疊方塊

所有會是從左往右, 並且從高度較低的位置開始堆疊

```py
min_height = min(height)
idx = height.index(min_height) # x軸, 擺放起始位置

r = idx+1 # x結尾位置
while r < m and height[r] == min_height:
    r += 1

# 最大能擺放的方塊為x, y軸兩方向的最小值: `max_possible_square = min(r-idx, n-min_height)`
# 由大到小嘗試擺放 -> backtracking
max_possible_square = min(r-idx, n-min_height)
for i in range(max_possible_square, 0, -1):
    # 放置當前方塊並更新高度
    new_height = height.copy()
    for j in range(i):
        new_height[idx+j] += i

    # backtracking
    dfs(new_height, moves+1)
```

base case:
1. 當heights[i]的高度全為n時代表我們塞滿整個tile
2. 一但當前backtracking所使用的方塊已超出當前最佳解, 提前終止backtracking