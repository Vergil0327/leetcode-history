# Intuition

divisor 越小，和越大
divisor 越大，和越小
可以看出來這有個極值存在，並且有單調性質
因此我們可以用binary search來猜這個divisor

而search space為 `[1, max(nums)]`，因為分母不可為0，而大過最大值時，全部除出來都會是零
因為要找的是`the smallest divisor`
所以如果當前的和比threshold還大，那我們divisor就繼續往大裡猜，降低算出來的和
反之divisor則往小裡猜

```py
l, r = 1, max(nums)
while l < r:
    mid = l + (r-l)//2
    SUM = check(mid)
    if SUM > threshold:
        l = mid+1
    else:
        r = mid
        
return l
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$