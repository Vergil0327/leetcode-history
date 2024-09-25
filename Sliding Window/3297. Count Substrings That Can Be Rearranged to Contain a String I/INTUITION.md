# Intuition

看到substring, 首先想到的是用sliding window找出含有word2 characters的substring (sliding window)

```py
# 示意圖:
# word1 = [X X X X X X O O O X O] ? ? ? ? ?
#          l                      r

target = Counter(word2)
count = Counter()

n = len(word1)
l = r = valid = res = 0
while r < n:
    ch = word1[r]
    count[ch] += 1
    if count[ch] == target[ch]:
        valid += 1
    r += 1

    while l < r and valid == len(target): # exist valid prefix substring in word1
        # TODO: how to calculate number of valid x ?

        count[word1[l]] -= 1
        if count[word1[l]] < target[word1[l]]:
            valid -= 1
        l += 1
return res
```

對於合法的這段substring word1[l:r], 他的右端點還有`n-r`個元素可延伸
相當於對於當前的合法sliding window來說, 他有`n-r+1`個合法右端點 => 代表當前的sliding window(substring)能貢獻`n-r+1`個valid string `x`

因此我們就在找到合法sliding window的同時, `res += n-r+1`即可
最終res就是total number of avlid substrings of word1


time: O(word1.size)
space: O(word1.size + word2.size)