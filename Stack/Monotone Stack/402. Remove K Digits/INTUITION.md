# Intuition

首先從Example 1:
`num = "1432219", k = 3, Output: "1219"`
可以很自然的想到，我們可以從字串中由左往右兩兩比較，刪除較大的那個數
看到前後字符比較，可以想到的是利用Stack

由於最後string要越小越好，因此我們要維護的其實就是個單調遞增的Monotonically Increasing Stack

同時由於我們僅能刪除的`k`個，因此我們最多就從Stack中pop掉`k`個，因此這裡的核心程式碼為:

```py
stack = []
canRemoved = k
for c in num:
    while canRemoved > 0 and stack and stack[-1] > c:
        stack.pop()
        canRemoved -= 1
    stack.append(c)
```

這樣最終Stack內的單調遞增序列就會是我們要的最小數列

但有個要特別注意的情況是，**萬一string一開始就是單調遞增的字符序列呢?**
ex. num="112", k=1, Output = "11"

這時候根本不會進入到while-loop去移除`k`個字符
因此再取最終結果之前必須先檢查，如果我們還有餘力可以移除，那就從最後開始移除。(因為stack維護的是單調遞增序列，越後面數值越大)

```py
while canRemoved:
    stack.pop()
    canRemoved -= 1
```

最後，在取得最終結果後，記得移除掉**leading zeros**並特別處理`res=""`的情況即可

- By Example3., if res == "": return "0" 
- Remove leading zeros
    ```py
    # remove leading zeros
    i = 0
    while i < len(res) and res[i] == "0":
        i += 1
    res = res[i:]
    ```

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$