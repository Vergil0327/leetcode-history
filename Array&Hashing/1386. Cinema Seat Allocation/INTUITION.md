# Intuition

正攻法:

```py
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = defaultdict(set)
        for r, c in reservedSeats:
            occupied[r].add(c)

        res = 0
        for row in range(1, n+1):
            # (row, 2)
            # (row, 3)
            # (row, 4)
            # (row, 5)
            empty = 2
            if 2 not in occupied[row] and 3 not in occupied[row] and 4 not in occupied[row] and 5 not in occupied[row]:
                res += 1
                empty -= 1

            # (row, 6)
            # (row, 7)
            # (row, 8)
            # (row, 9)
            if 6 not in occupied[row] and 7 not in occupied[row] and 8 not in occupied[row] and 9 not in occupied[row]:
                res += 1
                empty -= 1

            # (row, 4)
            # (row, 5)
            # (row, 6)
            # (row, 7)
            if empty==2 and 4 not in occupied[row] and 5 not in occupied[row] and 6 not in occupied[row] and 7 not in occupied[row]:
                res += 1
        return res
```

直接遍歷查看, 可能的四人位只有三種可能
但可惜會MLE


由於一排就十個座位, 我們hashmap可以改成利用bitmask來儲存座位狀態, 降低空間複雜度
並且我們只需要關注8個位置能不能湊成四人位即可: seat2+seat3, seat4+seat5, seat6+seat7, seat8+seat9

```py
occupied = defaultdict(int)
for r, c in reservedSeats:
    r, c = r-1, c-1
    occupied[r] |= (1<<c)

total = n * 2
for state in occupied.values():
    seat2 = (state>>1)&1
    seat3 = (state>>2)&1
    seat4 = (state>>3)&1
    seat5 = (state>>4)&1
    seat6 = (state>>5)&1
    seat7 = (state>>6)&1
    seat8 = (state>>7)&1
    seat9 = (state>>8)&1

    seat23, seat45, seat67, seat89 = seat2+seat3, seat4+seat5, seat6+seat7, seat8+seat9

    if seat45 == seat67 == 0:
        if seat23 > 0 or seat89 > 0:
            total -= 1
    elif seat45 == 0:
        if seat23 > 0:
            total -= 2
        else:
            total -= 1
    elif seat67 == 0:
        if seat89 > 0:
            total -= 2
        else:
            total -= 1
    else:
        total -= 2
return total
```

# Optimization

只要將4人座位分成三種情況: (2,3,4,5), (4,5,6,7), (6,7,8,9)
1. 如果(2,3,4,5)任一位置有人: 視作`狀況1`, 並用1個bit位來儲存代表該4人位已不合法
2. 如果(4,5,6,7)任一位置有人: 視作`狀況2`, 並用1個bit位來儲存代表該4人位已不合法
3. 如果(6,7,8,9)任一位置有人: 視作`狀況3`, 並用1個bit位來儲存代表該4人位已不合法

```py
seats = defaultdict(int)
for i, j in reservedSeats:
    if 2 <= j <= 5:
        seats[i] |= 1
    if 4 <= j <= 7:
        seats[i] |= 2
    if 6 <= j <= 9:
        seats[i] |= 4
```

那最終只要看是什麼狀況就能知道要扣掉多少非法4人座位
這概念很像是linux的`chmod`指令, 不同情形用不同數字, 看最後組合出的數字狀態即可知道情況

```py
res = 2 * n
for occupied in seats.values():
    if occupied == 7:
        res -= 2
    elif occupied:
        res -= 1

return res
```