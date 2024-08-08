# Intuition

想法是每次都從東方(右側)起點開始, 起點每次會往右shift一位
那我們持續記錄我們`shift`的變量, 也可順便計算出當前繞圈矩形的邊長`length = 2*shift+1`
那再來就是移動我們的當前位置`(r, c)`, 然後繞邊長一圈即可

# Concise implementation

1. 先往右
2. 往下
3. 往左
4. 往上

這樣一個循環, 然後沒當往右跟往左的時候, 我們走的步數要多一步

```py
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] # right, down, left, up
        
        res = [[rStart, cStart]]
        r, c = rStart, cStart
        length = d = 0 # move length step in d direction
        while len(res) < rows * cols:
            if d == 0 or d == 2: length += 1 # move to right or left, length of path require extra step

            # move circularly
            for _ in range(length):
                r += dirs[d][0]
                c += dirs[d][1]
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])

            d = (d+1)%4 # change to next direction
        return res
```