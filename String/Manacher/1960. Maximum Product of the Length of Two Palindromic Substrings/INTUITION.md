# Intuition

brute force => O(n^2), 嘗試每個作為中心 延展palindrome長度

特地提到為兩個**odd length**的palindrome

odd length => ****** X ******
以s[i]為中心的話:
用`s[i-1] == s[i+1]`這個條件可以找出palindrome 中心

而求出以各個s[i]為中心能延伸的palindrome長度 => Manacher Algorithm O(n)
可求出P[i]: the longest extended radius of the palindromic substring centered at i

定義:
- left[i]: the longest palindromic substring in s[0:i]
- right[i]: the longest palindromic substring in s[i+1:n-1]
我們要求的是: max(left[i] * right[i=1])

那麼left[i]該怎麼求?

```
s = {X X X X X X X X X X X X X X} X
                                  i
     {              j              }
```

dynamic programming:
1. left[i] >= left[i-1]
2. 藉由Manacher提供的P[i], 我們要從左往右移動`j`(雙指針)找到一個j+P[i] 剛好小於等於 `i`的地方, 也就是剛好涵蓋到`i`, 這時以`j`為半徑的palindrome長度就是`(i-j)*2+1`
3. left[i] = max(left[i-1], (i-j)*2 + 1) where j is middle of palindromic substring covered i

4. 實現起來就是
```py
j = 0
for i in range(n):
    while j < n and j+P[j] < i:
        j += 1
    left[i] = max(left[i-1], (i-j)*2 + 1)
```

right[i]就一樣概念, 改從右往左掃過來

最後遍歷一遍`i`找出: max(left[i]*right[i+1] for i in range(n-1))

## Manacher

[Explanation by @HuifengGuan](https://www.youtube.com/watch?v=dWn2QURs6sA&ab_channel=HuifengGuan)

持續紀錄更新`maxRight`, `maxCenter`

```
s = X {X X X X X X X X X X X} X X
           j     mC    i  mR
```

```py
n = len(s)
maxRight = maxCenter = -1
P = [0]*n

for i in range(n):
    if i <= maxRight:
        j = maxCenter*2-i # i, j對稱, j的index位置就等於maxCenter*2減去i那整段
        r = min(P[j], maxRight-i)
    else:
        r = 0

    # 試著拓展r
    while (i-r >= 0 and i+r < n) and s[i-r] == s[i+r]:
        r += 1
    
    P[i] = r-1

    # update maxRight and maxCenter back
    if i+P[i] > maxRight:
        maxRight = i+P[i]
        maxCenter = i
```

# Complexity

- time complexity: $O(n)$
- space complexity: $O(n)$