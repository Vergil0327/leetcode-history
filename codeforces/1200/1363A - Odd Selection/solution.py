"""
# Intuition

為確保和是奇數: 至少要有1個 odd number:

```py
if odd == 0:
    print("NO")
else:
    x -= 1
    odd -= 1
```

再來由於even再怎麼加都不會改變奇偶性, 而2個odd可以變成偶數
所以我們先取剩餘的奇數兩兩配對, 剩餘不夠的數目在用偶數來補
最終如果足夠取到x個, 那便是"YES", 不行則是"NO"
"""

t = int(input())

for _ in range(t):
    n, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    odd = even = 0
    for num in nums:
        if num%2 == 0:
            even += 1
        else:
            odd += 1
    
    if odd == 0:
        print("NO")
    else:
        x -= 1
        odd -= 1
        
        x -= min((x//2) * 2, (odd//2) * 2) # min(upperbound, remaining odd pair)
        x -= even
        if x <= 0:
            print("YES")
        else:
            print("NO")