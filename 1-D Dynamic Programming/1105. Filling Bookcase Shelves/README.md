[1105. Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/)

`Medium`

You are given an array `books` where `books[i] = [thicknessi, heighti]` indicates the thickness and height of the ith book. You are also given an integer `shelfWidth`.

We want to place these books in order onto bookcase shelves that have a total width `shelfWidth`.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to `shelfWidth`, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:

![img](shelves.png)

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example 2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4

Constraints:

- 1 <= books.length <= 1000
- 1 <= thicknessi <= shelfWidth <= 1000
- 1 <= heighti <= 1000

<details>
<summary>Hint</summary>

</details>


books = X X X X X X X [X X X X]
                       j     i -> thickness = sum(books[j:i]) <= shelfWidth
                               -> height = max(books[j:i])

considering i-th book, we can iterate backward to find `j-th` book such that books[j:i] is a valid level of shelf with max(books[j:i]) height and `sum(books[j:i])` thickness which should be <= shelfWidth.

thus, we can define dp in this way:
dp[i]: the minimum possible height that the total bookshelf can be after placing first `i` books

thus, the state transfer should be:
dp[i] = min(dp[i], dp[j-1] + max(books[j:i])) if sum(books[j:i]) <= shelfWidth

then, we can start coding

```py
n = len(books)
for i in range(n):
    height = 0
    thickness = 0
    for j in range(i, -1, -1):
        height = max(height, books[j][1])
        thickness += books[j][0]
        if thickness <= shelfWidth:
            dp[i] = min(dp[i], dp[j-1] + height)
        else:
            break

return dp[n-1]
```

since dp[j-1] will be dp[-1] if j = 0
we can either change books and dp to 1-indexed or handle j=0 (i.e. dp[i][0]) independently

let's iterate j within [1,i] and handle j=0 independently

if j=0, it means we select books[:i] as one level of shelf, therefore:

```py
height = thickness = 0
for i in range(n):
    height = max(height, books[i][1])
    thickness += books[i][0]
    if thickness <= shelfWidth:
        dp[i] = height
    else:
        break
```

and we can now iterate j from i to 1

```py
for i in range(n):
    height = 0
    thickness = 0
    for j in range(i, 0, -1):
        height = max(height, books[j][1])
        thickness += books[j][0]
        if thickness <= shelfWidth:
            dp[i] = min(dp[i], dp[j-1] + height)
        else:
            break
```