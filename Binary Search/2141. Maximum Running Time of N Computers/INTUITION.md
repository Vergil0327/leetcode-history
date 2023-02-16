# Intuition

這題很明顯可以試著用二分搜值來做，大體框架就是:
如果我們猜每台電腦都可以跑`mid`分鐘，那就用`canRun`來檢查看看對不對
```py
l, r = 0, sum(batteries)
while l < r:
    mid = r - (r-l)//2
    if canRun(mid):
        l = mid
    else:
        r = mid-1
return l
```

但問題是這個`canRun`該怎麼實作?

想法是如果本身電池就大於等於這個`mid`，那很好，能滿足的電腦直接加1，也不用想說要更換電池
但如果電池本身不夠用，那代表我們肯定會需要中途更換

只要電池累積到 >= mid，代表又能再跑一台電腦，我們累積電量就扣掉`mid`且能跑的`computer += 1`
並且有剩餘電量的電池能繼續給其他不夠跑足`mid`分鐘的電腦更換

所以實作為:

```py
def canRun(targetMinute):
    computer = accumulatePower = 0
    for battery in batteries:
        if battery >= targetMinute:
            computer += 1
            continue

        accumulatePower += battery
        if accumulatePower >= targetMinute:
            accumulatePower -= targetMinute
            computer += 1
    return computer >= n
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$

# Most Optimzed Solution

[Lee215](https://leetcode.com/problems/maximum-running-time-of-n-computers/solutions/1692939/java-c-python-sort-solution-with-explanation-o-mlogm/?orderBy=most_votes)

sum(batteries)/n is upperbound
if batteries[i] > sum(batteries)/n, it means 1 computer has been handled
and all we need to handle is `n-1` computer with `sum(batteries) - batteries[i]`

keep doing this until batteries[i] <= sum(batteries)/n, the rest of batteries are all we can use evenly

```py
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries)
        sumBattery = 0 
        for b in batteries:
            sumBattery += b 
        
        while batteries[-1] > sumBattery / n:
            n -= 1 
            sumBattery -= batteries.pop()

        return sumBattery // n
```