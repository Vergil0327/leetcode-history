# Intuition

ex.
```
(1,3), (2,4) => m = 1, b=y-x=2

(1,3), (0,4) => m = -1, b=y+x=4
```

we can use a hashmap to store how many lamps illuminates current cell grid[i][j],
i.e. hashmap = {[row or column or diagonal]: how many lamps illuminate contribute to this}

- we can hash diagnal with (m, b) as key
- hash row with (unique key, row) as key
- hash col with (unique key, col) as key

thus, we just use this hashmap to check if cell is illuminated or not and update this hashmap after queries[i]

根據以前做過N-Queen的經驗
所有對角線都可以根據國中數學`y = mx+b`來求出相對應的唯一hash
所以我們可以用hashmap記住每個lamp所照亮的每一個位置
row 跟 column斜率分別為 0 跟 inf, 但其實我們用任意unique作為key即可

並且題目有說lamp即時有重複, 仍代表該位置只有一個lamp
所以我們可以用hashset來去除重複

```py
LAMPS = set()
for lamp in lamps:
    LAMPS.add(tuple(lamp))

for i, j in LAMPS:
    # row
    illuminance[(ROW, i)] += 1
    # column
    illuminance[(COL, j)] += 1
    # diagonal
    illuminance[(1, j-i)] += 1
    illuminance[(-1, j+i)] += 1
```

再來就依序回答queries[i]並透過hashmap可判斷是否仍被照亮.
並且每次關掉一個lamp後, 便可以從hashset中移出進而更近一步提升判斷效率

- time comeplexity
$$O(len(lamps)+len(queries)*3*3)$$