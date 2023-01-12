# Intuition

這題要求的是有多少方法可以在切`k-1`刀分成k份後，每份都有蘋果
每次我們可以橫切或縱切，每次切完，剩下的Pizza也可以橫切或縱切，因此我們可以看到這是個遞歸形式的子問題，因此總共的方法數為:

total methods = 橫切 + 縱切
              = current row (has apple) * bottom piza + current col (has apple) * right pizza

定義 `DFS(row, col, k(刀))` 且因為是從上橫切，或從左縱切，所以我們的decision tree DFS從`(row, col)=(0, 0)`且有`k-1`刀可以切開始

每個決定就是橫切或縱切，總方法數就是全部加起來

```
methds = hasApple(current piaza with top slice) * DFS(bottom pizza, k-1) + hasApple(current pizza with left slice) * DFS(right pizza, k-1)
```

如果當前這份有蘋果，`hasApple()`則返回1，沒有則返回0
(或者也可以先用`hasApple()`判斷，有蘋果再遞歸)

**如何高速判斷有沒有蘋果? 如何實作hasApple?**

這題還有個最關鍵的是，我們必須要能快速知道當前切法有沒有蘋果

由於這題可以橫切或縱切，因此透過prefix sum row by row或column by column都沒能很有效解決

最好的方式是`leetcode 304`的方式： **prefix square sum**
再透過容斥原理(排容原理)可以很快求出當前matrix的prefix sum

# Complexity

- time complexity
$$O(ROWS * COLS * K)$$

- space complexity
$$O(ROWS * COLS)$$