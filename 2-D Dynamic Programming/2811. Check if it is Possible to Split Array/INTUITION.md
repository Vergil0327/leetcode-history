# Intuition

這題是要判斷是否能分成n個subarray並且每個subarray長度至少為1

每次都分成兩個subarray, 如果這兩個subarray都滿足以下任一條件, 那才是個合法的split
1. len(subarray) == 1
2. sum(subarray) >= m

```
arr = {XXXXX}{XXXX}
        A      B
```

所以對於當前subarray, 我們用左右兩端點定義一個array然後遍歷split的位置將array分成A, B兩個subarray:
```py
def dfs(l, r):
    if l >= r: return 0 # zero split
    if r-l+1 == 2: return 1 # 1 valid split, each subarray has length == 1
    
    res = 0
    for i in range(l, r):
        sumA = presum[i+1]-presum[l]
        sumB = presum[r+1]-presum[i+1]
        if ((sumA >= m or i-l+1 == 1) and (sumB >= m or r-i == 1)):
            res = max(res, dfs(l, i) + dfs(i+1, r)+1)
    return res
```

只要兩個subarray都滿足上述兩條件其中一個, 那就是個合法的split
我們就看當前nums能有多少個合法的split, n個subarray需要n-1個split, 最後就看split的數目有沒有大於等於n-1即可
