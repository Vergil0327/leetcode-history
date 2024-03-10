# Intuition

strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1
(-1)^{i+1} * sum[i] * (x - i + 1) over all i's such that 1 <= i <= x.


並且每個subarray必須互不相交(disjoint)
根據constraint: `1 <= n * k <= 10^6`, 首先想到的是TC: O(nk)的dynamic programming

但這題題意很爛, 看下兩個例子

nums=[1,2,3,-1,2], k=3, expected=22
nums=[-1,1,2,3,2], k=3, expected=5

原本預期應該都是{1,2,3}*3 + {-1}*(-2) + {2}*1
最大subarray當分配做1st subarray, 此時x=3, 然後依序下去

但實際上卻是:
1. {1,2,3}*3 + {-1}*(-2) + {2}*1
2. {-1,1,2}*3 + {3}*(-2) + {2}*1

所以實際上考慮前i個elements時, 第一個subarray永遠是乘上`k`, 第二個乘上`-(k-1)`, 依序下去

那這樣的話我們其實一個一個element來看:

```
{X X X X X X X X} X
                  i
```

對於i-th element來說, 我們可以選擇接在前一個subarray後面繼續下去, 也可以跳過, 也可以自立門戶
但對於i-th element來說自立門戶跟繼續接在當前subarray的分數並不同, 所以除了`i`, `k`外
我們還必須有個True/False變數來記錄當前的subarray還可不可以繼續append下去
定義`dfs(i, k, appending): the maximum possible strength considering first i elements and selecting k disjoint subarrays. current status is appending`

起始狀態為**dfs(0, k, False)**, 當前沒有subarray正在appending, 從0-th element開始, strength係數從`k`開始, 分別為`k`, `-(k-1)`, `k-2`, ...

那狀態轉移我們就考慮i-th element就好, 我們考慮選來繼續append或不選:

1. 選擇i-th element作為subarray: dfs(i+1, k, True) + nums[i] * k * (1 if k%2 == 1 else -1)
2. 不選擇i-th element, 那麼我們就看`appending`這個變數:
    - 如果當前有個appending到一半的subarray, 那麼相當於我們subarray停止在`i-1`的位置, 並且不選i-th element: 下一round `k`變為`k-1`: if appending: dfs(i+1, k+1, False)
    - 如果當前沒有正在append的subarray, 那麼`k`不變 (因為還沒開始製造係數為`k`的subarray): if not appending: dfs(i+1, k, False)

整體框架為:

```py
def dfs(i, k, appending):
    # pick i-th element to append/create subarray
    res = dfs(i+1, k, True) + nums[i]*k*(1 if k%2 == 1 else -1)

    # skip i-th element
    if appending:
        res = max(res, dfs(i, k-1, False))
    else:
        res = max(res, dfs(i+1, k, False))
    return res
```

而遞歸肯定要有base case:

最直覺的就是:
1. if k == 0: return 0 => 代表已經選完k個subarray
2. 那如果我們考慮完 整個nums了呢?, 那就看我們滿足`k`個subarray沒:
    - 如果考慮完整個nums, 但還沒選完k個subarray, 那就return `-inf`
    - 如果當前正好是第`k`個subarray, 此時係數為1, **並且已經有值了**, 亦即`k==1 and appending`, 那此時則返回`0`

所以兩個base就是:
```py
if k == 0: return 0
if i == n:
    if k == 1 and appending: return 0
    return -inf
```

TC: $O(n * k * 2)$

但下面這寫法會MLE, 所以我們額外開個空間出來, 用多維矩陣會比較省空間
```py
@cache
def dfs(i, k, appending):
    if k == 0: return 0
    if i == n:
        if k == 1 and appending: return 0
        return -inf

    res = dfs(i+1, k, True) + nums[i]*k*(1 if k%2 == 1 else -1)
    if appending:
        res = max(res, dfs(i, k-1, False))
    else:
        res = max(res, dfs(i+1, k, False))
    return res
return dfs(0, k, False)
```

```py
memo = [[[inf, inf] for _ in range(k+1)] for _ in range(n+1)]
def dfs(i, k, appending):
    if k == 0: return 0
    if i == n:
        if k == 1 and appending: return 0
        return -inf

    if memo[i][k][appending] < inf: return memo[i][k][appending]

    memo[i][k][appending] = dfs(i+1, k, 1) + nums[i]*k*(1 if k%2 == 1 else -1)
    if appending:
        memo[i][k][appending] = max(memo[i][k][appending], dfs(i, k-1, 0))
    else:
        memo[i][k][appending] = max(memo[i][k][appending], dfs(i+1, k, 0))

    return memo[i][k][appending]
return dfs(0, k, 0)
```