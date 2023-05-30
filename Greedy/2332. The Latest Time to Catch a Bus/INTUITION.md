# Intuition

首先肯定是按照時間順序排序
```py
buses.sort()
passengers.sort()
```

然後模擬乘客上車, 直到最後一台車後分兩種情形討論:
```py
m, n = len(buses), len(passengers)
cap = j = 0
for i in range(m):
    cap = capacity # reset current capacity
    while j < n and passengers[j] <= buses[i] and cap > 0:
        cap -= 1
        j += 1
```

最後一個上車的乘客為: `j-1` # last person step into the bus

1. 這時如果還沒滿, 那就準時抵達即可
  - 返回`buses[m-1]`
  - 但可能也有人也在這時刻(`buses[m-1]`)抵達, 所以得往前找, 直到passengers[j]跟passengers[j+1]之間有個空白時段能讓我們插隊, 這時我們就插在passengers[j+1]的前一秒抵達即可
    ```py
    if passengers[j] == buses[m-1]:
        j -= 1
        while j >= 0 and passengers[j]+1 == passengers[j+1]:
            j -= 1
        return passengers[j+1]-1
    ```
2. 如果滿了, 就從最後一個人往前找, 最後一個人的前一秒沒人抵達, 那我們這時抵達即可
    ```py
    while j-1 >= 0 and passengers[j]-1 == passengers[j-1]:
        j -= 1
    return passengers[j]-1
    ```
