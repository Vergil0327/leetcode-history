# Intuition

我們要找的是相同元素的interval sum
所以可以先用hashmap把相同元素的位置座標找出來

```py
n = len(arr)
v2idx = defaultdict(list)
for i in range(n):
    v2idx[arr[i]].append(i)
```

再來我們看interval sum如何計算

```
x: indices [a, b, x, d, e]
                  i

=> interval_sum = sum(|x-a|, |x-b|, |x-x|, |x-d|, |x-e|)
```


看到絕對值我們就先把它拆掉試試: `x-a + x-b + x-x + -(x-d) + -(x-e)`

很明顯可看出可以前後半段分開討論, 以`x-x=0`為中間點拆成前後:

1. x+x - (a+b) = i * x - sum(a, b, ...)
2. (d+e) - (x+d) = sum(d, e, ...) - (n-i) * x
    
很明顯`sum(...)`的部分都是一段區間和
所以我們可以提前計算prefix sum, 然後遍歷每個位置以O(1)時間計算出interval sum


time: O(n)