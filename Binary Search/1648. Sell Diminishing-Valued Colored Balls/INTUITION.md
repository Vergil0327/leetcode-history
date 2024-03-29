# Intuition

這題首先想到的是，最佳解就是貪心地先取最大分數的球

那這樣的話每顆球會是由大到小一個一個取，最多就取`orders`個
這邊猜的值是要取到值到什麼程度為止

假設我們取到`mid`為止，這樣每顆球能取的分數就是:
`(inventory[i]-mid)*(inventory[i]-mid+1)//2 if inventory[i] > mid`

    [1,2,3,7,8,9] 取到 `mid=4`
->  [1,2,3,4,4,4] -> total score = (7+6+5) + (8+7+6+5) + (9+8+7+6+5)
->                                  取3個       取4個        取5個

然後我們判斷:
- 如果這個threshold能取的球大於`orders`個，代表我們threshold猜的太小了
- 如果這個threshold能取的球小於等於`orders`個，代表我們可以繼續再往小裡猜，並且也可能是個解，只要我們再多娶幾個比threshold小的數取到`orders`個，一樣是會是個合法的答案，只是不一定是最大值

因此binary search框架為:

```py
l, r = 1, int(1e9)
while l < r:
    mid = l + (r-l)//2
    if count(mid) <= orders:
        r = mid
    else:
        l = mid+1
```

最後收斂到的`l`就是我們的目標threshold
然後我們在遍歷一遍計算分數即可，但要注意的是`count(targetPrice)`可能沒取完全部`orders`

所以最終答案記得把`剩下的單數*(target price - 1)`加上

```py
targetPrice = l
answer = 0
for ball in inventory:
    if ball < targetPrice: continue
    answer = (answer + (ball+targetPrice)*(ball-targetPrice+1)//2)%MOD

remainOrder = orders - count(targetPrice)
answer += (targetPrice-1)*remainOrder
```

可以這樣進行binary search是因為我們一定是從最大的分數開始取
一個一個取，每個球的分數都會是單調遞減的
所以我們猜的threshold一定有機會被取到，然後就能透過取到的單數來判斷我們猜的太低或太高

# Other Solution

排序後由大到小來取inventory[i], 如果inventory[i]一直拿拿到inventory[i+1]都還有剩orders
那就直接透過數學計算, batch calculation

並且下一輪我們相當於有2個inventory[i]
```
inventory = [X Y Z] -> [Y Y Z] -> [Z Z Z] where X > Y > Z
```

```py
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10**9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)

        n = len(inventory)
        cnt = 1 # number of inventory[i]
        res = 0
        for i in range(n-1):
            if cnt*(inventory[i] - inventory[i+1]) < orders: 
                res += cnt*(inventory[i] + inventory[i+1]+1)*(inventory[i]-inventory[i+1])//2 # arithmic sum
                res %= mod

                orders -= cnt*(inventory[i] - inventory[i+1])
            else: 
                # 目前有 cnt 個 inventory[i]
                m, r = divmod(orders, cnt)
                res += cnt*(inventory[i] + inventory[i]-m+1) * m//2 # arithmic sum
                # 經過上面拿取步驟, 此時inventory[i] = inventory[i]-m
                # 還剩下r個order要拿
                res += r*(inventory[i] - m)
                res %= mod
                break

            cnt += 1
        return res
```