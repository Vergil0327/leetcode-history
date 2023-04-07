# Intuition

這題如果不暴力解的話其實很難，這題跟[395. Longest Substring with At Least K Repeating Characters](../395.%20Longest%20Substring%20with%20At%20Least%20K%20Repeating%20Characters/)很像

雖然是要找substring/subarray, 但卻無法用two pointers/sliding window來解
必須加上限制才能讓sliding window的左右邊界順利移動，而不是右邊界直衝到底

這題解法一樣一樣是對sliding window內所能包含的字母種類加上限制
我們規定sliding window內的字母至多只能包含m種字母, 然後我們從1到26遍歷m
這樣我們就能分情況用sliding window討論:

我們持續移動右邊界，一但window內的字母種類超過`m`種，我們就移動左邊界縮小window
合法條件就是一但window內的種類等於`m`時, 代表此時的sliding window可能有解
此時我們再判斷:
    - sliding window內的字母是否大小寫都包含在內
    - 如果都有包含並且長度比原本`res`還長, 那就更新`res`

```py
for m in range(1, 26+1):
    # sliding window here
```

由於我們要知道sliding window的種類
所以我們用個hashmap `window`紀錄**每個字母的小寫**, 用來判斷window內包含的字母種類
並且再額外用個hashmap `count`紀錄每個字母在window內的次數, 這用來判斷window內是否包含該字母的大寫以及小寫

那麼sliding window的邏輯就出來了:

以下是個左閉右開的區間: **[l:r)**

```py
l = r = 0
window = defaultdict(int)
count = defaultdict(int)

while r < n:
    # 我們持續移動`r`並記錄種類及次數
    count[s[r]] += 1
    window[s[r].lower()] += 1
    r += 1

    # 一但種類超過`m`種，就移動左邊界
    while l < r and len(window) > m:
        count[s[l]] -= 1
        window[s[l].lower()] -= 1
        if count[s[l]] == 0: del count[s[l]]
        if window[s[l].lower()] == 0: del window[s[l].lower()]
        l += 1
    
    # 合法條件就是當 window內種類等於m時，此時檢查該substring是否包含兩種字母的大小寫
    if r-l > len(res) and len(window) == m and all((count[ch.lower()]> 0 and count[ch.upper()]) for ch in window):
        # 更新res
        if len(s[l:r]) > len(res):
            res = s[l:r]
```

# Complexity

- time complexity
$$O(26n)$$

# Optimized Solution

跟395. Longest Substring with At Least K Repeating Characters一樣
這題一樣能用Divide & Counquer來解

思路也是一樣，首先找出害群之馬
假如某個character `s[i]` 他的lowercase或是uppercase不存在於s裡的話
代表可行解只存在於s[:i]跟s[i+1:]內，我們就遞歸搜尋這兩個substring
直到整個string內的每個字符的大小寫都包含在內，我們就返回該string
然後在全部結果中取長度最長的

```py
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        characters = set(s)
        for i, ch in enumerate(s):
            if ch.lower() not in characters or ch.upper() not in characters:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s
```