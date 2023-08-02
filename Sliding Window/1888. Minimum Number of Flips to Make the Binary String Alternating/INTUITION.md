# Intuition

最終目標就是轉換成兩種情況:
1. 0101010101..., 0開頭
2. 1010101010..., 1開頭

```
s =     YXXXXXXXXXXXXXX
target: 0101010101010101
        1010101010101010
```

由於我們可以rotate `s`, 仔細觀察會發現每當我們移動首字母到尾巴時, 中間的difference都是不變的
所以我們可以用O(1)時間來計算出每次rotate對difference的影響
```
next round:

s =      XXXXXXXXXXXXXXY
target: 0101010101010101
        1010101010101010
```

所以我們可以把最終兩種目標string構造出來, 分別是`alt0`、`alt1`
並同時計算當前`s`對於這兩種的difference是多少

```py
alt0 = alt1 = ""
diff0 = diff1 = 0
for i, ch in enumerate(s):
    if i%2 == 0:
        alt0 += "0"
        alt1 += "1"
        if ch == "0":
            diff1 += 1
        else:
            diff0 += 1
    else:
        alt0 += "1"
        alt1 += "0"
        if ch == "0":
            diff0 += 1
        else:
            diff1 += 1
```

那再來就開始對s進行rotate, 這邊用個deque來模擬
對於s[i]來說:
- 如果s[i] == alt0[i], 代表對於alt0來說, 原本合法的s[i]少了一個, 所以`diff0 += 1`
- 如果s[i] == alt1[i], 代表對於alt1來說, 原本合法的s[i]少了一個, 所以`diff1 += 1`
- 再來就是如果 s[i] == alt0[i+n], 那麼代表`diff0 -= 1`
- 再來就是如果 s[i] == alt1[i+n], 那麼代表`diff1 -= 1`

最後我們對於每次rotate都取個全局最小的`min(diff0, diff1)`即可

所以上面構造的`alt0`, `alt1`要延伸至`2n`長度:

- 如果n為偶數, 那麼`alt0 += alt0`, `alt1 += alt1`
- 如果n為奇數, 那麼會是`alt = alt0+alt1`, `alt1 = alt1+alt0`

```
010 => 010101
101 => 101010
0101 => 01010101
1010 => 10101010
```