# Intuition

我們要求的是替換掉最短長度的subarray使得`s` balanced

比較常與subarray有關聯的就是移動左右邊界來找出目標subarray

這題對於balance的定義使得`Q`, `W`, `E`, `R`的個數有了個數上的限制，代表我們可以透過整體個數來移動左右邊界，並透過左右邊界來定義subarray

這題突破口是，如果要讓整個`s` balanced, 我們要找的那段subarray就是扣除掉那段subarray的字符後，subarray以外的部分全都是小於等於`n//4`的

所以我們可以先計算`Q`, `W`, `E`, `R`的個數, 並且如果已經平衡了那就直接返回`0`
```py
counter = Counter(s)
if counter["Q"] == required and counter["W"] == required and counter["E"] == required and counter["R"] == required:
            return 0
```

再來我們就可以透過Two Pointers (或稱Sliding Window)來找出所有subarray使得subarray以外的`Q`, `W`, `E`, `R`個數都小於等於`n//4`

我們目標是盡可能移動右邊界

一但`Q`, `W`, `E`, `R`個數都小於等於`n//4`後, 就代表扣除當下的subarray後已經balanced了
我們就可以移動左邊界, 繼續找下個目標subarray:

整體架構如下, [l, r) 左閉右開
```py
l = r = 0
res = n
while r < n:
    counter[s[r]] -= 1
    r += 1

    # logic here - 1

    while l < r and (counter["Q"] <= required and counter["W"] <= required and counter["E"] <= required and counter["R"] <= required):
        # logic here - 2
        counter[s[l]] += 1
        l += 1
    # logic here - 3
```

那麼計算邏輯通常就放在comment所示的那三個地方
由於我們要找的是一段subarray使得QWER個數都小於等於`n//4`, 所以很自然的我們應該要把計算的部分放在`# logic here - 2`

```py
# logic here - 2
res = min(res, r-l)
```

