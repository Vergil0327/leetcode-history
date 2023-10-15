# Intuition

brute froce的話會發現整個matrix的乘積會很大, 這會造成運算超時(TLE)
由於product matrix的定義是除了grid[i][j]本身以外的所有乘積
所以可以想到其實就是這(i,j)位置的prefix_product * suffix_product

因此我們可以把整個grid打平, 然後求出每個(i,j)位置的prefix_produxt和suffix_product
並記得對`12345`取餘

```py
vals = [v for row in grid for v in row]

length = len(vals)
prefix = [1]*length
for i in range(length):
    prefix[i] = (prefix[i-1] if i-1>=0 else 1) * vals[i] % mod

suffix = [1] * length
for i in range(length-1, -1, -1):
    suffix[i] = (suffix[i+1] if i+1 < length else 1) * vals[i] % mod
```

那這樣我們就能透過: product[i][j] = prefix_i_j * suffix_i_j %mod 還原整個product matrix

```py
product_mat = []
rows = []
for i in range(length):
    p = prefix[i-1] if i-1 >= 0 else 1
    s = suffix[i+1] if i+1 < length else 1
    rows.append(p*s%mod)
    if len(rows) == n:
        product_mat.append(rows)
        rows = []

return product_mat
```