# Intuition

以這題的數據量來說, 其實O(n^2)的brute force方式即可

```py
def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    indices = [set()]
    for i in range(n):
        indices.append(indices[-1].copy() if boxes[i] == "0" else indices[-1] | {i})

    res = []
    for i in range(n):
        index = indices[i] | (indices[n] - indices[i+1])
        dist = 0
        for j in index:
            dist += abs(j-i)
        res.append(dist)
    return res
```

但這題時間上其實是可以O(n)的, 僅需要3-pass

每個位置`i`都要考慮左邊"1"需要多少swap, 右邊"1"需要多少swap
比起遍歷`i`然後再計算左邊、右邊swap次數

我們可以先預計算**每個位置`i`需要多少swap來移動左邊的"1"**以及計算**每個位置`i`需要多少swap來移動右邊的"1"**
這樣就能在O(n)遍歷期間以O(1)查詢每個位置`i`的所需swap


1. 首先定義`left_moves[i]`: the minimum number of moves to swap all the "1" to `i` position from the left

```py
left_moves = [0] * n
num_boxes = 0
for i in range(n):
    left_moves[i] = (left_moves[i-1] if i-1>=0 else 0) + num_boxes
    num_boxes += int(boxes[i] == '1')
```

2. `right_moves[i]`: the minimum number of moves to swap all the "1" to `i` position from the right

```py
# number of steps for boxes from right
right_moves = [0] * (n+1)
num_boxes = 0
for i in range(n-1,-1,-1):
    right_moves[i] = right_moves[i+1]+num_boxes
    num_boxes += int(boxes[i] == '1')
```

3. 那這樣我們最後就只需要在遍歷一遍找出每個`i`位置從左、從右需要移動多少swap即可
   - `answer = [left_moves[i] + right_moves[i] for i in range(n)]`

time: O(n)
space: O(n)