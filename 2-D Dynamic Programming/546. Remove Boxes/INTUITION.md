# Intuition

從brute force來看，對於一個連續數來說，最大得分有兩種可能

1. 先拿分
2. 跟後面相同數接在一起後，在拿分

因此這題的解答是在額外帶入一個參數來剪枝，提高DFS的搜索效率

ex.
boxes = [OOOO XXXXXX OO XXX OO]
         l            j   i  r, where count = 2 (= # of O after i)
對於 boxes[r] = `O`來說
可能的得分有:
1. boxes[l:i] + (r-i) * (r-i): 取走最後兩個`O`得分後，考慮剩下的boxes[l:i]
2. (boxes[l:j] + boxes[i+1:r]) + boxes[j+1:i]: 先取走`XXX`，也就是先取走boxes[j+1:i]得分後，考慮boxes[l:j]+boxes[i+1:r]拼接後的得分, 其中 `l <= j <= i`

帶入額外的參數後，比起brute force全部每個位置都盲目考慮
我們簡化成兩種
1. 直接取走最後`OO`然後得分
2. 考慮對於任意`index=j`且可以跟最後的`OO`相連接時的聯合得分，也就是我們先取走中間所有`X`後的聯合得分

如此一來便大大提高搜索的效率

```py
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        cache = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(l, r, tailNumCount):
            if l > r: return 0

            if cache[l][r][tailNumCount] != -1:
                return cache[l][r][tailNumCount]

            i = r
            count = tailNumCount
            while i >= l and boxes[i] == boxes[r]:
                count += 1
                i -= 1
            
            # OO XXXXXX OO XXX OO
            # l              i  r, where count = 2 (= # of O after i)
            cache[l][r][tailNumCount] = dfs(l, i, 0) + count * count

            # OOOO XXXXXX OO XXX OO
            # l  j         j   i  r
            for j in range(i, l-1, -1):
                if boxes[j] == boxes[r] and boxes[j+1] != boxes[r]:
                    cache[l][r][tailNumCount] = max(cache[l][r][tailNumCount], dfs(l, j, count) + dfs(j+1, i, 0))

            return cache[l][r][tailNumCount]
        
        return dfs(0, len(boxes)-1, 0)
```