# Intuition

最直覺就是直接建構出BST然後在建構過程中順便更新深度

但還有另一種方法是利用SortedDict, 就像是C++的Map

我們首先把上下界加入到SortedDict中: {-inf: 0, inf: 0}
key-value分別是: {node_value: 深度}

對於每個要插入到BST的node_value來說，我們用bisect_right (C++的upperbound) 找出位置
該位置就是第一個大於他的節點，可能是根節點也可能是右邊界，因此我們插入的節點深度就是這兩個點的深度取max+1

```
order = [2,1,4,3]
{-inf: 0, inf: 0}
{-inf: 0, 2: 1, inf: 0}
{-inf: 0, 1: 2, 2: 1, inf: 0}
{-inf: 0, 1: 2, 2: 1, 4: 2 inf: 0} -> 插入4時是i=3, max(depth[2], depth[inf])+1 = max(1,0)+1 = 1+1 = 2
{-inf: 0, 1: 2, 2: 1, 3: 3 4: 2 inf: 0}
```

```py
depths = sortedcontainers.SortedDict({float("-inf"):0, float("inf"):0})

for x in order:
    i = depths.bisect_right(x)
    depths[x] = max(values_view[i-1:i+1])+1
```

這概念類似解法可參考[HuifengGuan](https://github.com/wisdompeak/LeetCode/tree/master/Tree/1902.Depth-of-BST-Given-Insertion-Order)

