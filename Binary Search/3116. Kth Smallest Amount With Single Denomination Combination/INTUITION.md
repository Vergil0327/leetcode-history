# Intuition

- 1 <= coins.length <= 15
- 1 <= coins[i] <= 25
- 1 <= k <= 2 * 10^9

coins長度不長且很小, 但k值很大, 大到10^9
brute force會是用min heap: O(k log(coins.length))而超時

```py
def findKthSmallest(self, coins: List[int], k: int) -> int:
    pq = [(c, c) for c in coins]
    heapq.heapify(pq)

    while k:
        n, c = heapq.heappop(pq)
        res = n

        heapq.heappush(pq, (n+c, c))
        k -= 1
    return pq[0][0]
```


但像是k-th smallest這類型的題目, 比較直覺能想到的是用binary search去猜這個k-th smallest amount `m`. (leetcode有相當多這類型的題目)
然後再看猜測的這個值是不是能貢獻k個multiples, 但計算過程裡面會有duplicates, 所以可能會需要排容原理來去除掉公倍數所貢獻的multiples
我們要找的就是第一個貢獻`k`個數的multiples

框架大概長這樣:
```py
def findKthSmallest(self, coins: List[int], k: int) -> int:
    coins.sort()
    n = len(coins)

    l, r = coins[0], coins[-1]*k
    while l < r:
        mid = l + (r-l)//2
        if count(mid) < k:
            l = mid+1
        else:
            r = mid
    return l
```

但就卡在這個helper function `count` 不知該如何下手

但後來想想, 排容原理就是:
每個coins[i]有m//coins[i]個multiples - 任意倆倆pair組合 + 任意三對組合 - ... + ...

所以用bitmask來標示選取的coins[i], 配合iterate all n-bit state where thare are m 1-bits的技巧
計算出當前的選擇能貢獻多少multiples

- 當選擇奇數個coins時, 根據排容是加法, 必須加上小於`m`的情況下, 這些選擇的最小公倍數會貢獻多少multiples
- 當選擇偶數個coins時, 則是減法, 我們必須扣掉小於`m`的情況下, 他們的最小公倍數會貢獻多少個duplicate

```py
def count(m):
    count = 0
    for i in range(1, n+1):
        state = (1<<i)-1
        while state < (1<<n):
            if i%2 == 1:
                count += countMultiples(state, m)
            else:
                count -= countMultiples(state, m)
            c = state & -state
            r = state+c
            state = (((r^state)>>2)//c) | r

    return count
```

而counMultiples很簡單, 就是計算最小公倍數LCM然後再看會貢獻多少個multiples:

```py
def countMultiples(state, m):
    choice = []
    for i in range(n):
        if (state>>i)&1:
            choice.append(coins[i])
    lcm = 1
    for c in choice:
        lcm = lcm*c//gcd(lcm, c)
    return m // lcm
```

而這可以更近一步簡化成

```py
def countMultiples(state, m):
    lcm = 1
    for i in range(n):
        if (state>>i)&1:
            lcm = lcm*coins[i]//gcd(lcm, coins[i])
    
    return m // lcm
```