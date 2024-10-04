# Intuition

這題看題目數據, 看起來是需要o(n) 或 O(nlogn)
由於是要找substring, 首先想到的是sliding window
我們可以利用hashmap來記錄當前的sliding window是不是有足夠的vowel跟consonant

但我們現在要的是滿足**至少5種vowels**以及**恰好k個consonant**

適合用在sliding window的條件, 僅能是**至少**
對於這種**恰好k個**的這類條件, 必須利用到[992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description/)這題的技巧

```
exactly K valid count = sliding_window_at_most(k) - sliding_window_at_most(k-1)
```

所以如果我們能知道**滿足至少5種vowels且至少有k個consonant**的合法substring個數, 假設是X, 的話
只要將這個個數減去**滿足至少5種vowels且至少有k-1個consonant**的合法substring個數, 假設是Y

那麼`X-Y`就是我們所求的**滿足5種vowels且洽好有k個consonant**的合法substring個數

在解決第一個困難點後
再來就是看我們能不能透過sliding window去找出滿足**至少5種vowels且至少有k個consonant**的合法substring個數

```
X X X X I X E X A X O X U
l       i               r
```

如上所示, 我們首先持續移動右端點`r`, 直到滿足條件
一但**consonant個數超過k個**就移動左端點`l`
然後看這時滿足**至少5種vowels且至少有k個consonant**有幾個?

> 答案是`i-l+1`個

這代表我們需要知道的是滿足5種vowel條件時, 最左側vowel的index位置, 所以整體框架為:

```py
def atMost(k):
    if k < 0: return 0 # 由於我們會需要求`k-1`, 一但k=0會變負數
    
    n = len(word)
    l = r = numVowels = valid = 0
    pos = {}
    for r in range(n):
        ch = word[r]
        if ch in "aeiou":
            numVowels += 1

            # if ch not in pos: # 第一個合法vowel
            #     valid += 1
            #     pos[ch] = r
            # else:
            #     if pos[ch] < l:
            #         valid += 1 # 第一個合法vowel
            #     pos[ch] = r
            # 上面整理一下變成:
            if ch not in pos or pos[ch] < l: # 第一個合法vowel
                valid += 1
            pos[ch] = r
        
        while r-l+1 - numVowels > k:
            ch = word[l]
            if ch in "aeiou":
                if pos[ch] == l:
                    valid -= 1
                numVowels -= 1

            l += 1

        if valid == 5:
            rr = min(pos["a"], pos["e"], pos["i"], pos["o"], pos["u"])
            res += rr-l+1
    return res
```

所以有了這個helper func後, 最終答案就是`atMost(k) - atMost(k-1)`

time: O(n)
space: O(1)

# Intuition2

有另個不錯的解法是由[@HuifengGuan](https://www.youtube.com/watch?v=2uxZjd5CK8k&t=21s&ab_channel=HuifengGuan)所講解的One Pass解法
也很直覺

同樣是利用雙指針去找出合法的sliding window
我們就看固定合法左端點時, 有多少個合法右端點

首先我們必須移動右端點直到滿足**5種vowels且consonant個數大於等於k**
那這樣我們分2種情況討論:

1. 5種vowels, consonant == k:
   - 這種情況下, 首先本身就是個合法substring, 再來我們就看右端點能向右延伸多少
   - 右端點能延伸的情況就看有多少個**連續母音**, 這樣consonant才會維持在`k`個
2. 5種vowels, consonant > k:
   - 不合法

```
X X X X X X X X X X X A E I X X
l                   r
```

所以當前以`l`為左端點的合法substring有: `1 + consecutive[r+1]`種

因此我們就持續維護左右端點計算總和即可

### 計算從`i`位置開始有多少個連續母音

```py
consecutiveVowel = [0] * (n+2)
for i in range(n-1, -1, -1):
    if word[i] in "aeiou":
        consecutiveVowel[i] = consecutiveVowel[i+1] + 1
```

### Sliding Window

```py
n = len(word)

valid = numConsonant = r = res = 0
vowels = Counter() # only 5 vowels
for l in range(n):
    # 移動右端點直到條件符合 valid == 5 and numConsonant >= k
    while r < n and (valid < 5 or numConsonant < k):
        if word[r] in "aeiou":
            vowels[word[r]] += 1
            if vowels[word[r]] == 1:
                valid += 1
        else:
            numConsonant += 1
        r += 1

    if valid == 5 and numConsonant == k:
        res += 1 + consecutiveVowel[r]

    # 移動左端點並維護vowels, valid & numConsonant
    if word[l] in "aeiou":
        vowels[word[l]] -= 1
        if vowels[word[l]] == 0:
            valid -= 1
    else:
        numConsonant -= 1
return res
```

time: O(n)
space: O(1)