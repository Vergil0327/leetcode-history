# Intuition

robot1有n個轉折點, 所以我們可以事先計算上下兩行的prefix sum

那們我們就能遍歷這個轉折點`i`, 這時:

1. robot1走的路徑為(0,0) -> (0,i) -> (1,i) -> (1, n-1)
2. 所以上下兩行分別剩下:
   1. top_remain = presum1[n]-presum1[i+1]
   2. bottom_remain = presum2[i]
   3. 這時robot2肯定是上下兩路選總和較大的走： `max(top_remain, bottom_remain)`

由於robo1要做的是minimize robot2's collection, 所以我們最終對robot2取`min`

```py
presum1 = list(accumulate(grid[0], initial=0))
presum2 = list(accumulate(grid[1], initial=0))

collect = presum1[-1] + presum2[-1]
for i in range(n):
    top_remain = presum1[n]-presum1[i+1]
    bottom_remain = presum2[i]
    robot2 = max(top_remain, bottom_remain)
    collect = min(collect, robot2)
return collect
```