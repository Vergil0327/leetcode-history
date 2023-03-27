# Intuition

對於石頭相消，表達成序列會是這樣的形式

[a, b, c, d, e, f, g]
|a-b| +/- |c-d| +/- |e-f| +/- g
|a-c| +/- |b-d| +/- |e-f| +/- g
...

```
例如 Example 1.
[2,7,4,1,8,1]
 - - + - + +
```

那答案就相當於我們對任一stones[i]前面加上正負號後的總和，並且總和要 >= 0

所以我們可以用一個hashset紀錄我們當前的石頭總重
對於當前的stones[i]來說, 我們可以對每個可能總重 +/- stones[i]
那這樣我們就從前一個狀態轉移到當前第i輪的狀態，其中hashset記錄所有可能的重量狀態

由於石頭相消的策略保證了最終答案必定是正數, 所以最後答案就是最小且大於等於0的石頭總重
>If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
