# Sorted List

## Intuition

每次加入一個數 `num` 後，小於 `num` 的個數與大於 `num`的個數取最小值為cost，加總即為所求
代表如果我們維護一個有序數列，我們則可以透過binary search搜尋上下界來迅速找出小於跟大於`num`的個數

使用 bisect_insort 會是個$O(N^2)$的解法，會超時
但如果使用但如果使用`SortedList`的話，則可以將時間複雜度降至$O(nlogn)$

```python
# Brute Force
def createSortedArray(self, instructions: List[int]) -> int:
    MOD = 10**9+7
    nums = []
    cost = 0
    for num in instructions:
        i = bisect.bisect_left(nums, num)
        j = bisect.bisect_right(nums, num)
        n = len(nums)
        bisect.insort_left(nums, num)
    
        cost += min(i, n-j)
        cost %= MOD
    return cost
```

# Complexity

- time complexity:

$O(nlogn)$

- space complexity

$$O(n)$$

# Segment Tree - method 1

## Intuition

這題也可以用線段數來做，做法有兩種

第一種是將原本的`instructions`裡的每個dinstinct number排序後，將數值對應到排序的index
這樣我們每次query某個數時，只要找尋她的左區間與右區間，即可得到比他小的數及比他大的數有多少
然後再把他更新進去

ex. instructions = [1,5,6,2] -> 去除重複且排序後相當於[1,2,5,6]
因此數值對應的index分別為:

num to index:
```
{
    1:0,
    5:2,
    6:3,
    2:1
}
```

這樣當我們遍歷時
```
for num in instructions:
    num = 1 -> index = 0 -> segment tree = [0,0,0,0]
    此時左半邊個數總和為0，右半邊個數也為0,因此cost = min(0,0)
    更新進去segment tree後變為[1,0,0,0]

    num = 5 -> index = 2 -> segment tree = [1,0,0,0]
    index=2的左半邊個數為1，右半邊個數為0，因此cost = min(1,0)
    更新進去segment tree後變為[1,0,1,0]

    以此類推...
```

# Complexity

- time complexity:

$O(nlogn)$

- space complexity

$$O(n)$$

# Segment Tree - method 2

## Intuition

第二種離散方法為將線段數的大小定為`max(instructions)`

類似把數值範圍從小到大都開一個bucket組成segment tree, 整個segment tree大小為 2*`max(instructions)`

這樣每次query就可以直接找，對於該數值 `num`，小於他的有多少及大於他的有多少
一樣可以快速找出左右兩區間個數，並且這種方法就不用先對 `instructions` 去除重複數後找個數值排序後的index

# Complexity

- time complexity:

$O(nlogm)$

m: max(instructions)

- space complexity

$$O(n)$$