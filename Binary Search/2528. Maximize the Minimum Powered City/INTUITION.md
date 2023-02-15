# Intuition

這題需要找極值，Maximum minimal required power for each city
既然是要把power分配給每個城市，因此我們可以嘗試用binary serach去猜這個極值

high level的核心程式碼思想為:

power在[0,sum(stations)+k]這個區間內，是否可以找出一個`mid`可以讓每個城市至少有`mid`個power，然後逐漸往upperbound去找

```py
lo, hi = 0, sum(stations) + k
while lo < hi:
    mid = hi - (hi-lo)//2
    if isValidPower(mid):
        lo = mid
    else:
        hi = mid - 1
return lo
```

根據題意，每個城市的power會是個sliding window的總和
因此在`isValidPower`裡，我們計算每個城市的power是否足夠`mid`

```
for i-th city
sliding window sum = [:r] + stations[i+r] - stations[i-r-1]
```

- 超過則沒事
- 不足的話則看我們加上額外的電力`k`後是否能滿足
  - 這裡有個**Greedy**的思想是，對於第`i`個之前的city都是滿足條件的，因此我們可以不用管
  - 為了讓加蓋的電力站能涵蓋最多城市，同時又能填補目前第`i`個城市的電力缺口，因此我們應當在`i+r`這個位置加上額外的電力
  - 所以我們另外用一個`additional`的數組來記錄我們在第幾個城市補上額外的電力`k`
    - 或者我們直接copy stations

    ```py
    n = len(stations)
    def checkPowerValid(target, k):
        cities = stations.copy()

        currPow = sum(cities[:r])
        for i in range(n):
            if i+r<n:
                currPow = currPow + cities[i+r]
            
            if currPow < target:
                if k < target-currPow: return False # we can't afford this target power
                diff = target-currPow
                cities[min(i+r, n-1)] += diff
                currPow += diff
                k -= diff

            if i-r >= 0:
                currPow -= cities[i-r]
        return True
    ```

# Complexity

- time complexity
$$O(n * log(sum(stations)+k))$$

- space complexity
$$O(n)$$