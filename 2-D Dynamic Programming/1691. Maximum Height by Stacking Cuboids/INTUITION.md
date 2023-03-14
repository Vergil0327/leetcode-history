# Intuition

這題最重要的是**排序**

由於我們要堆疊箱子並且確保上面的箱子在長寬高**三個維度**都比下面的箱子還要小
由於我們要求的是最大高度，因此我們可以對三個維度排序，讓最大維度作為高
再利用剩下的兩個維度來堆疊

```py
# make largest value be height
for i in range(n):
    cuboids[i].sort()
```

再來由於底下的箱子在三個維度都要大於上面的箱子
因此我們在對整體箱子做排序，首先想到的是**對高度做排序**
但由於箱子可能會出現相同高度，又相同寬度的情況，因此我們其實三個維度都要排序
這樣才能確保我們會盡可能挑大的當底座

```py
cuboids.sort(key=lambda x:(-x[2], -x[0], -x[1]))
```
*注意必須得三個維度都排序，不然在兩個維度相同的情況下，我們有可能會先挑到較小的而錯失堆疊的機會*


排序完後，看來就是個DP問題了，我們可以這樣定義DP:

`dp[i]: the maximum height considering stacked cuboids[:i]`

那狀態轉移就是，我們考慮第`i`個箱子要堆疊在哪一堆的上面
所以我們往前找一個最大的`j`疊上去，由於已經做過排序，所以我們總是會優先處理三個維度相對大的

X X X X X X X [X]
      j        i

首先對於i來說，如果前面都疊不上那我們可以自立門戶，所以初始值為自身高度
```py
for i in range(n):
    w, l, h = cuboids[i][0], cuboids[i][1], cuboids[i][2]
    dp[i] = max(dp[i], h)
```

再來就是往前找一個最大的j疊上去，由於我們可以任意旋轉長寬，所以只要長寬兩個維度可以比底下的小即可進行狀態轉移
```py
for i in range(n):
    w, l, h = cuboids[i][0], cuboids[i][1], cuboids[i][2]
    
    dp[i] = max(dp[i], h)
    for j in range(i):
        if (cuboids[j][0] >= w and cuboids[j][1] >= l) or (cuboids[j][1] >= w and cuboids[j][0] >= l):
            dp[i] = max(dp[i], dp[j] + h)
```

那最後答案就是在全部可能的堆疊裡找一個最大的, `max(dp)`