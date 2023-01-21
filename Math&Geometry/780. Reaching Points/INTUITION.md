# Intuition

[Great Explanation here from Lee215](https://leetcode.com/problems/reaching-points/solutions/114856/java-c-python-modulo-from-the-end/?orderBy=most_votes)

如果起點可以走到終點，那終點也能返回起點
起點往終點的有太多選擇，我們不好找出該怎麼走到targetX跟targetY
但從終點返回，肯定只會有一個方式

而(targetX, targetY) = (x + ky, y + kx)，如果我們類似這麼做的話

```py
while tx > sx and ty > sy:
    if ty > tx:
        ty -= tx
    else:
        tx -= ty
```

遇到 (1,1) 走到 (100000000000000,1)這樣的case的話便會直接超時
因此比較好的做法是取mod來縮減 x = x+ky, y = y+kx 的那個k倍數

# Approach

因此我們從終點開始往回走，由於`x = x+ky`, `y = y+kx`
因此我們相互對x, y中較大的數取餘走回起點

```py
while tx > sx and ty > sy:
    if ty > tx:
        ty %= tx
    else:
        tx %= ty
```

跳出while-loop後，有可能
1. tx 仍大於 sx
2. ty 仍大於 sy
3. 相等或走過頭

其中能走回起點的case為:
1. tx 等於 sx，那麼此時 (ty-sy)%sx 必定要等於零且 ty >= sy
2. ty 等於 sy，那麼此時 (tx-sx)%sy 必定要等於零且 tx >= sx
3. 除此之外代表無法走回起點或是已經走過頭，返回False

# Complexity

- time
$$O(log(min(tx, ty)))$$

- space

$$O(1)$$