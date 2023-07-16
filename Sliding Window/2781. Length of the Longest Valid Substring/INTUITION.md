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