# Binary Search

## Intuition

首先我們可以確認如果互不相同的數小於K的話則無解
並且因為我們要找的是k個互不相同的數，因此我們可以先將price array去除重複的數值

再來我們看`tastiness`的定義，當
- 若`tastiness`越大，則能找到符合的數越少
- 若`tastiness`越小，能找到符合的數則越多

因此我們可以嘗試用`binary search`來猜出`tastiness`的極值

由於`tastiness`的定義為兩個數的差，因此search space則為 `0` 到 `max(price)-min(price`)`

引此當我們猜某個`tastiness`值時，假設該值為`mid`，只要我們能找出至少`k`個數組成後最小差值為`mid`，則可以提高lowerbound，反之則縮減upperbound

核心程式碼為
```python
l, r = 0, max(price)-min(price)
while l < r:
    mid = r - (r-l)//2
    if check(price, mid):
        l = mid
    else:
        r = mid-1
return l
```

而我們的`check`函式, 我們可以先將`price`排序
首先我們先取第一個值後，(也就是最小的值，因為這樣跟後續的值的差最有可能大於等於目標`mid`值)，由小到大(也就是由左往右)遍歷

每當找到一個值與我們上個取走的值之間的差大於等於`mid`時，代表我們可以取走，當最後所有取值的數目大於等於`k`時，代表我們目前猜得`mid`是可行的，可以提高lowerbound，反之則減少upperbound


```python
# if maximum tastiness is mid, check if we can greedily pick k prices[i] which abs distance is >= mid in O(n)
def check(prices, target):
    cnt = 1
    lastTaken = prices[0]
    for i in range(1, n):
        if prices[i]-lastTaken>=target:
            cnt += 1
            lastTaken = prices[i]
    return cnt >= k
```

反覆搜索後即可得到答案

## Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$