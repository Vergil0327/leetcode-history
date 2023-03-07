# Intuition - GREEDY

這題想法是:
1. 只要有聲"c"，那代表有一隻青蛙剛叫
2. 只要有聲"k"，代表一隻青蛙叫完

當情況1發生時，`frogs + 1`
當情況2發生時，`frogs - 1`

然後看整個過程中，最多需要幾隻青蛙，即為答案
維護一個 `maxFrogs = max(maxFrogs, forgs)`

然後記得排除掉不可能的情況

1. 如果叫聲次數不一致，那肯定不對
```py
counter = Counter(croakOfFrogs)
if counter["c"] != counter["r"] or counter["r"] != counter["o"] or counter["o"] != counter["a"] or counter["a"] != counter["k"]: return -1
```

2. 叫聲順序不合法, ex. `kaocr`

順序必須是 c -> r -> o -> a -> k
所以如果有任一叫聲次數比前一個少的話，那肯定是不對的，直接返回`-1`