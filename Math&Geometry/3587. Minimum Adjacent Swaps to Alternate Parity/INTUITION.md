# Intuition

找出奇數, 偶數的位置index, 然後優先排除**無解**的狀況

```py
if abs(len(even) - len(odd)) > 1: return -1
```

然後嘗試:

1. 將偶數放置到偶數位置
2. 將偶數放置到奇數位置

swap的次數為`abs(original position - expected position)`的總和
然後返回可能情況的最小值即可
