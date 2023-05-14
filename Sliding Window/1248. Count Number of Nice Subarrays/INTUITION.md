# Intuition

看到要計算有多少個含有k個奇數的subarray, 首先看到subarray
聯想到的就是透過two pointers來確定左右邊界, 然後透過`k`這個條件來滑動左右邊界計算

程式碼如下
```py
n = len(nums)
l = r = odd = res = 0
while r < n:
    if nums[r]%2 == 1:
        odd += 1
    r += 1

    while l < r and odd > k:
        if nums[l]%2 == 1:
            odd -= 1
        l += 1
    if odd == k:
        res += 1
return res
```

但這樣會發現Example 3只會計算到這四個subarrray

```
[2, 2, 2, 1, 2, 2, 1]
[2, 2, 2, 1, 2, 2, 1, 2]
[2, 2, 2, 1, 2, 2, 1, 2, 2]
[2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
```

但實際上答案是16
原因是中間的`1221`subarray的左右各有3個偶數
所以算上左右邊界後, 實際上是**4*4**種subarray

```
2,2,2 [1,2,2,1] 2,2,2
l l l  l     r  r r r
```

這時Example 3的計算方式就是我們主要的突破口
我們應該要滑動窗口直到`# of odd number == k`時, 我們看左右邊界分別能外延伸多少
這時所能形成的合法subarray為左邊界的合法個數`left`乘上右邊界的合法個數`right`
如上圖所示, 左邊界`l`共有四個合法位置而右邊界`r`也有四個合法位置, 所以`left * right = 4*4 = 16`

因此我們真正關心的就是每個odd number的index位置, 而even number並不重要

所以我們用`odd`來儲存每個odd number的index
```py
odd = []
for i, num in enumerate(nums):
    if num%2 == 1:
        odd.append(i)
```

這樣一來, 每當我們sliding window滑到符合條件的情況時, 亦即`cnt == k`時
我們便計算左右邊界的合法個數, 相乘即為當次左右邊界所能貢獻的所有subarray
```py
res = 0
l = r = cnt = 0
n = len(odd)
while r < n:
    num = odd[r]
    cnt += 1
    r += 1

    if l < r and cnt == k:
        # 計算 left & right
        left = odd[l]-(odd[l-1] if l-1 >= 0 else -1)
        right = (odd[r]-num) if r < n else (len(nums)-num)
        res += left*right
        
        cnt -= 1
        l += 1
```

- `left`可以透過odd[l] - odd[l-1]得到
  - 但要注意`l-1`可能會越界, 只有在`l-1>=0`時才符合
  - edge case: 如果`odd[l]=0`, 這時我們希望的`left`為1, 所以`odd[l-1] if l-1 >= 0 else -1`. 這樣一來odd[l]-odd[l-1] = 0 - (-1) = 1
  - `left = odd[l]-(odd[l-1] if l-1 >= 0 else -1)`

- `right`可以透過odd[r+1] - odd[r]得到
  - 一樣注意r+1可能會越界, 只有在`r+1<len(odd)`時才成立
  - edge case, 當`r=n-1`時, 這時我們代表右邊界已經到底, 這時我們希望`right=1`. 所以這時odd[r+1] = len(odd), 這樣`odd[r+1]-odd[r] = n - (n-1) = 1`
  - `right = (odd[r]-num) if r < n else (len(nums)-num)`

這樣一來, 我們每當滑到一個合法窗口
便能計算到當前的左右邊界所能形成的所有subarray

# Other Solution

這想法跟上面是一樣的, 重點就是每個奇數的中間間隔偶數有多少
一但符合條件, 哪些偶數都可以延伸成為邊界
而`cur_sub_cnt`就是計算`left`跟`right`

在**while**裡面計算的部分就是`left`, 而下方`res += cur_sub_cnt`計算的就是`right`

```
{X X X X X X} [O X X O] {X X X X X X X} O ...
 cur_sub_cnt              cur_sub_cnt
```


```py
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    n = len(nums)
    odd_cnt = 0
    res = 0
    cur_sub_cnt =0
    
    l = 0
    for r in range(n):
        if (nums[r] % 2) != 0:
            odd_cnt += 1
            cur_sub_cnt = 0

        while (odd_cnt == k):
            if nums[l] % 2 != 0:
                odd_cnt -= 1
            cur_sub_cnt += 1 # left
            l += 1

        res += cur_sub_cnt # right
    return res
```