# Intuition - Sliding Window

substring可以透過two pointers, `l`&`r`來標示
先想有沒有辦法用sliding window

```
[X X] X X X
 l r
```

如果[l:r]是合法的且word[l:r]不存在forbidden內的話
下次的[l:r']範圍, 我們只需要判斷[left:r'] where l <= left < r'有沒有存在於forbidden內即可
因為這代表固定右邊界為word[r]時, 所有左邊合法左邊界與右邊界`r`所組成的subarray都是合法的


```
# next interation

[X X X] X X
 l   r'
```

這時如果存在一個[left:r']存在於forbidden的話, 則更新`l = left+1`並直接跳出
不然的話就代表固定r'這個右邊界所能貢獻的subarray [left:r']都是合法的

並且這邊還可以多個條件是: 由於我們前面可先計算出`maxLength(forbidden)`
這樣我們在檢查[left:r']存不存在於forbidden內時, 如果這個window超出maxLen的話肯定不會出現在forbidden內
我們就不用再繼續檢查了, 可以直接跳出

# Other Solution

一樣概念
```
X X X X [X X X X X X X X X X] X
         i                 j
```

定義dp[i]: the longest valid length starting at i

我們可以找出以`i`為左端點的每個subarray的合法最長長度, 由於forbidden內的長度不超過10
所以我們可以用`O(10n * string slice O(10))`來找出有沒有存在一個不合法的forbidden string
如果長度超出10都沒找到的話, 那也不用再找了, 代表以`i`為左端點一路到最後都沒有forbidden string

# Core Concept

其實不管是第一種還是第二種解法
最重要的是要從後往前遍歷來找出非法端點後, 排除掉最遠端點

以brute force來說會是這樣
```py
for i in range(n):
    for j in range(i, n):
        # ...
```

如果由左到右的話每次都要重新找右端點
但從右往左的話我們可以用一個數組紀錄當前合法最右端點

因為如果像下圖一樣, [i:j]為forbidden[k]的話
那麼以i為左端點的位置第一個非法右端點為`j`, 也表示word[i:j-1](both inclusive)為以i為左端點的最長substring

```
X X X X X X X [X X X] X
            i' i   j
```

在下一輪`i'`時, 我們也只需要檢查到`min(i'+10, j)`即可
這時最長substring長度為[i':j-1] (both inclusive) => `length = j-i' = dp[i]-i'`
不能包含到j, 不然的話[i':j]就會包含forbidden[i:j]
所以從右到左遍歷，反過來找dp[i]的話, 才能沿用資訊

第一個sliding window解法也是一樣概念，只是他是排除左端點
但也是由後往前遍歷:
`word[left:r] in forbidden => l = left+1 排除左端點使得[l:r]為最長合法substring`
