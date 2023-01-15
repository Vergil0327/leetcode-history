# Intuition

```
queries = [(0,0,2,2), (1,1,3,3)]

1   0   1   -1  0
0   1'  0   1'  0
1   0   1   0   0
0   1'  0   1'  0
0   0   0   0   0
```

M = len(matrix)
我們可以把matrix想成有M個difference array

當只有一維array時，我們可以透過標記起點與終點來達到O(n)時間加總所有計算
例如如果我們要讓 index [0,3], [2,6] 全部區間加1的話，我們可以透過在`index=0, 2的位置+= 1`，然後在`index=3, 6的後一個位置-=1`
ex. nums = [1,0,1,0,-1,0,0,-1,0]
這樣我們就可以用O(n)的時間，透過 nums[i] += nums[i-1]來得到我們要的以O(n)時間達到多個 range update

因此我們把matrix想成多個difference array後，對於每個query:
- 在每個ROW標記 +=1
- 在COL+1的位置標記 -= 1

```
for r1,c1,r2,c2 in queries:
    for r in range(r1, r2+1):
        mat[r][c1] += 1
        if c2+1 < n:
            mat[r][c2+1] -= 1
```

最後在透過O(N * N)的時間一次更新即可

# Complexity

- time complexity
$$O(len(queries) * N + N*N)$$

- space complexity

$$O(N^2)$$