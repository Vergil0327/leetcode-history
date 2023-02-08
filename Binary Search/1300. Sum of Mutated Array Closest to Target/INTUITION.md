# Intuition

當我們的threshold猜的值越大，總和越大
反之如果猜得越小，就會越多值被壓下來，總和就越小

但前提是，`arr`的總和大於target
要是總和就小於target了，你的threshold會一直往上猜

ex. arr = [2,3,5], target = 11

因此這個edge case要特別單獨處理，使得binary search成立

**edge case**
當總和小於`target`時，best value就是所有數值裡面最大的數

那再來就是要如何binary search?

收斂到最後，有可能最佳值帶有小數點，這時最佳值有可能是使得總和小於`target`的數，也可能是總和大於`target`的數

例如這種情況
best value = mid 時   -> SUM < target
best value = mid+1 時 -> SUM > target

這時候我們就要兩個比較看哪個比較近就選哪個
如果都等於`target`，那就選值較小的`mid`

因此我們binary search要找的是:
使得總和盡可能剛好小於target的值

因此binary search的架構為
```py
l, r = 0, 100000
while l < r:
    mid = r - (r-l)//2
    SUM = calculate(mid)
    if SUM < target:
        l = mid
    else:
        r = mid-1
return l if abs(calculate(l)-target) <= abs(calculate(l+1)-target) else l+1
```

**helper function**

那至於helper function `calculate`的實踐有兩種方法

1. 最簡單的就是O(n)的算法，直接帶入threshold加總一遍即可
  ```py
  def calculate(value):
      total = 0
      for num in arr:
          total += min(num, value)
      return total
  ```

2. 另外一種是O(logn)的算法，但會需要先對`arr`做排序，所以最終還是O(nlogn)
   1. 先對`arr`排序，然後求出prefix sum
   2. 用binary search找出lowerbound，也就是第一個大於等於threshold的值的位置
   3. 大於threshold的部分就是:`(n-i)*threshold`
   4. 小於的部分就直接用prefix sum求即可: `prefixSum[i]`
   5. 最終總和就是: `(n-i)*threshold + prefixSum[i]`, where i = bisect.bisect_left(arr, threshold)

# Complexity

- time complexity

$$O(nlogn)$$