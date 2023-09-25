# Intuition

restrictions[i] = [xi, yi] means person xi and person yi cannot become friends, either directly or indirectly.

這種僅需判斷有沒有在同個group的, 首先想到的是union-find

對於requests[i] = [u,v]來說, 一但u跟v可以成為friend, 那就把他們union起來, 然後令result[i] = True
這樣後續如果requests[j]已經間接成為friend了, 就可直接result[j]=True

那再來就要想如何判斷request[i]有沒有受到某個restrictions[j]所影響
不能成為朋友的條件是u的朋友圈跟v的朋友圈裡, 有任意配對出現在restriction裡

反過來說, 也就是當restriction[i] = [x, y], x跟y分別出現在u與v的朋友圈中
所以我們可以遍歷restriction[i] = [x,y]然後看:

1. 如果`x`跟`u`在同一個朋友圈且`y`跟`v`在同個朋友圈
2. 或是如果`y`跟`u`在同一個朋友圈且`x`跟`v`在同個朋友圈

的話, 就代表`requests[i] = [u, v]`不能成為朋友, `res[i] = False`

# Complexity

- time:

$$O(n^2)$$