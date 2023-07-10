# Intuition

```
LXXLXRLXXL
XLLXRXLXLX
```

XL -> LX => L能往左移動
RX -> XR => R能往右移動

所以我們可以用two pointers, `i` and `j`來一一比對
首先遍歷end[i]查看每個不是"X"的位置:
1. 如果end[i] == "L", 移動`j`找出start[j]第一個不為X的字母
    - 合法的條件為: start[j] == "L" 並且由於"L"能往左移動, 所以`j >= i`都可以
    - 其餘條件返回False
2. 同理如果end[i] == "R", 必須滿足end[j] == "R" and j <= i
3. 注意, 以上能正確的前提是Counter(start) == Counter(end)

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$