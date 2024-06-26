# Intuition

1 pair  -> 1
2 pairs -> 2
3 pairs -> 5
4 pairs ->

```
   2
 1   3
8     4
 7   5
   6
```

想成一個arr的話如下:

```
X X X X X X X X X X X X X X
                j   j   j i
```

`1-indexed`
考慮第i個人能有多少握手方式, 其中i為偶數
i可以跟j握手:
  - 跟j=i-1握手, 然後左邊剩下的`j`人各自握手
  - j=(i-1)-2握手, 這樣右手邊保證i-1跟i-2兩個人能握手, 左手邊則有i-1-2人各自握手
  - j=(i-1-2)-2握手, 右手邊有4人, 左手邊有j人
  - ...

所以定義dp[i]為i個人的握手方案, 那麼
```
dp[i] = 第i人握手後, 方法數=左手邊人數互握方法數 x 右手邊人數互握方法數
            => 左邊有j人, 右邊有i-j-2人
            => 左右兩邊能任意握 => 最終可能的方法數為左邊方法數乘上右邊方法數
      = sum(dp[j] * dp[i-j-2]) where j = 0, 2, 4, ..., i-2
```

**base case**

dp[1] = 0
dp[2] = 1