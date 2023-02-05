# Intuition

以這個範例來看
Input: arr = [2,3,4,7,11], k = 5
The missing positive integers are [1,5,6,8,9,10,12,13,...]

當我們的搜索範圍為 [0,n]時，`arr[mid]-(mid+1)`就是missing的個數
所以如果`missing < k`的話，我們就提高下界`l = mid+1`
`missing >= k`的話，就縮小上界`r = mid`

這樣最後會收斂在 `l=r` 的地方，此時的`l`就會是我們使用的missing個數
例如這個範例最終會收斂在 `l = r = 4`
代表missing前面已經用了4個，無論這四個數是什麼，我們要求得第k個missing就是 `l+k`

前面missing使用了4個，無論這四個數是什麼:
ex. [2,3,4,7] 或 [1,2,3,4]
我們要求的missing裡的第5個數都會是9
前面使用的個數後的第k個數，那就是`l+k`

# Complexity

- time complexity
$$O(logn)$$

- space complexity
$$O(1)$$