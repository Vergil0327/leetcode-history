# Intuition

題目看似複雜, 但由於所有合金必須都得在同一台machine生成, 所以我們就看每個machine最多能生成幾個alloy即可
因此我們要找的是一個upperbound, 所以可以透過binary search來找出這個值

對於每個machine `i`來說, 我們先找到他的seach space:

首先我們遍歷合金`j`：
我們當前庫存有stock[j]個, 因此我們省下了`stock[j]*cost[j]`的budget

所以假設其他材料都充足的話, 當前的buget最多可以買`ceil(budget+stock[j]*cost[j]/cost[j])`個材料
假設所需composite[i][j]為最小值1, 就代表我們最多可以做出這麼多個合金
這樣遍歷完後就能得到我們可能的最大製作合金數目
```py
l = r = 0
for j in range(n):
    r = max(r, (budget+stock[j]*cost[j])//cost[j]+1)
```

有了search space再來就是一般的binary search

```py
# 遍歷 machine `i`
while l < r:
    mid = r - (r-l)//2
    if check(i, mid):
        l = mid
    else:
        r = mid-1
res = max(res, l)
```

判斷當前猜測的製作合金數目`mid`合不合法就看我們budget夠不夠

我們所需的費用`need`為: (製作單個合金的所需材料數 * 合金數目 - 當前材料的庫存) * 材料成本
```py
def check(i, mid):
    need = 0
    for j in range(n):
        need += max(0, composition[i][j]*mid - stock[j]) * cost[j]
    return need <= budget
```