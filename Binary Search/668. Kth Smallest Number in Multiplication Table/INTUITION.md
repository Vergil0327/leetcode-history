# Intuition

只要是我們的搜索範圍是有序的，並且我們要找出極值或是猜某個值，我們都可以考慮binary search適不適用

由於乘法表是個Sorted Matrix，因此我們可以用二分搜值的方法找出目標值

至於要怎麼找出當前的值是第幾小的數的話，由於Matrix的ROW跟COLUMN都是有序的，因此我們可以從左下角出發，會發現這樣的matrix有個特性

1. 每當當前的值 >= 目標時，這整個column都會 >= 目標值，都可加入count，然後Column往右移一位
2. 每當當前的值 < 目標時，我們就往上移一個ROW，然後再回到第一步繼續判斷
這樣搜索會發現我們會沿著對角線，從左下往右上搜索，等到我們越界後代表我們已經搜索完有多少個值小於等於當前的值

搜索程式碼如下:
```py
# For sorted matrix
def count(num):
    r, c = m, 1
    count = 0
    while r > 0 and c <= n:
        if r * c <= num:
            count += r
            c += 1
        else:
            r -= 1
    return count
```

至於binary search則為:
```
l, r = 1, m * n
while l < r:
    mid = l + (r-l)//2
    if count(mid) < k:
        l = mid+1
    else:
        r = mid
```
整個二分搜索完後， l = r = answer

# Optimized

另外搜索其實有個更快搜索方式
由於這是個乘法表，我們只要看value在每個row的位置 `value//row_i` 然後加上即可
但由於我們最多只有`n`個column，所以上限為 `min(num//i, n)`

```
def count(num):
    count = 0
    for i in range(1, m+1):
        count += min(num // i, n)
    return count
```

# Complexity

- time complexity
$$O(mlog(m*n))$$

- space complexity

$$O(1)$$