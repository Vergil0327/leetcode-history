# Intuition

1. 拿走i-th元素後就不能再取相鄰元素
2. 首尾相連, 想成一個環
3. 會正好從3n slices中取走n個pizza

首尾相連, 取走後相鄰元素不能再取 => 這題最難的第一個突破口就是, 題意所描述的狀態其實就是house robber II
必須聯想到house robber II才能做這道題
而對於要考慮環狀取法的house robber II, 由於首尾不會同時取到, 所以可以拆解成兩個house robber I來從所有可行的取法中找出最優解
最終再取全局最優: **max(house_robber(slices[0:n-1]), house_robber(slices[1:n]))**

對於house robber, 我們定義:

dp0[i] = max(dp0[i-1], dp1[i-1]) => 不取i-th element, 從前面i-1個元素找出最優
dp1[i] = dp0[i-1] + slices[i] => 取i-th element, 由於相鄰元素不可取, 只能從dp0[i-1]狀態轉移過來

但由於我們最多只能取(3n/3)個pizza slices, 所以我們再多加個數量的約束, 定義:
dp0[i][m]: the maximum slices we can get if we **skip** i-th element considering first i element and take m slices so far
dp1[i][m]: the maximum slices we can get if we **take** i-th element considering first i element and take m slices so far

那狀態轉移就是:

```py
def house_robber(start, end, size):
    dp0 = [[0]*(size+1) for _ in range(end+1)]
    dp1 = [[0]*(size+1) for _ in range(end+1)]

    for i in range(start, end+1):
        for m in range(1, min(size, i-start+1)+1):
            dp0[i][m] = max(dp0[i-1][m], dp1[i-1][m])
            dp1[i][m] = dp0[i-1][m-1] + slices[i]
    return max(dp0[end][size], dp1[end][size])
```

由於在start=0時, dp前驅狀態i-1會是-1, 所以我們預先處理i=start時的狀態, 然後i從start+1開始

那麼在i=start時的base case:
- dp0[start][0]: 我們不取第start個, 此時總共取了0個
- dp1[start][1]: 我們取了第start個, 此時總共取了1個

而且別忘記我們在更新dp1[i][m]時也會用到`m-1`時的狀態, 所以m從1開始
而m=0代表什麼都沒取, 手上獲得的slices為0, 正好就是我們的初始狀態

```py
dp0[start][0] = 0
dp1[start][1] = slices[start]

for i in range(start+1, end+1):
    for m in range(0, min(size, i-start+1)+1):
        dp0[i][m] = max(dp0[i-1][m], dp1[i-1][m])
        dp1[i][m] = dp0[i-1][m-1] + slices[i]
```