# Intuition

把正負號全部拆開

```
abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).

eq = |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        正數或負數              正數或負數          正數或負數
   = max(
       arr1[i] - arr1[j] + arr2[i] - arr2[j]  + i - j = (arr1[i]+arr2[i]+i)  - (arr1[j]+arr2[j]+j) = Xi-Xj
       arr1[i] - arr1[j] - arr2[i] + arr2[j]  + i - j = (arr1[i]-arr2[i]+i)  - (arr1[j]-arr2[j]+j) = Xi-Xj
       -arr1[i] + arr1[j] + arr2[i] - arr2[j] + i - j = (-arr1[i]+arr2[i]+i) - (-arr1[j]+arr2[j]+j) = Xi-Xj
       -arr1[i] + arr1[j] - arr2[i] + arr2[j] + i - j = (-arr1[i]-arr2[i]+i) - (-arr2[i]-arr2[j]+j) = Xi-Xj

       arr1[i] - arr1[j] + arr2[i] - arr2[j]  - i + j = (arr1[i]+arr2[i]-i)  - (arr1[j]+arr2[j]-j) = Xi-Xj
       arr1[i] - arr1[j] - arr2[i] + arr2[j]  - i + j = (arr1[i]-arr2[i]-i)  - (arr1[j]-arr2[j]-j) = Xi-Xj
       -arr1[i] + arr1[j] + arr2[i] - arr2[j] - i + j = (-arr1[i]+arr2[i]-i) - (-arr1[j]+arr2[j]-j) = Xi-Xj
       -arr1[i] + arr1[j] - arr2[i] + arr2[j] - i + j = (-arr1[i]-arr2[i]-i) - (-arr2[i]-arr2[j]-j) = Xi-Xj
     )
```

create all possible max X array and find:
`answer = {max(X)-min(X) for all possible X} where X = arr1[i]+arr2[i]+i, arr1[i]-arr2[i]+i, ...`

```py
def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    arrs = [[] for _ in range(8)]
    for i, (A,B)  in enumerate(zip(arr1, arr2)):
        arrs[0].append(A+B+i)
        arrs[1].append(A-B+i)
        arrs[2].append(-A+B+i)
        arrs[3].append(-A-B+i)
        arrs[4].append(A+B-i)
        arrs[5].append(A-B-i)
        arrs[6].append(-A+B-i)
        arrs[7].append(-A-B-i)

    res = 0
    for arr in arrs:
        arr.sort()
        res = max(res, arr[-1]-arr[0])
    return res
```

# General Expression

但其實拆開絕對值就是每個數都可正可負拆開, 也就是找出所有正負號的組合然後求解
所以比起hard code所有組合, 我們可以寫成程式碼的形式

定義arr = (arr1[i], arr2[i], i)
1. 用2進制代表每個數的正負號:
    - 111: arr[i] = arr1[i]+arr2[i]+i
    - 000: arr[i] = (-arr1[i]) + (-arr2[i]) + (-i)

2. find max(arr[i]) and min(arr[i])

3. res = max{max(arr[i]) - min(arr[i])}