# Intuition

目的是要求出所有subarray的number of unique element的中位數
首先試試brute force O(n^2):

```py
uniqueness = []
for i in range(n):
    distinct = set()
    for j in range(i, n):
        distinct.add(nums[j])
        uniqueness.append(len(distinct))
uniqueness.sort()

return uniqueness[(len(uniqueness)-1)//2]
```

但仍然沒啥想法, subarray共有n*(n+1)/2個, 時間上至少會是O(n^2)
1 <= nums.length <= 10^5 => brute force遍歷每個subarray肯定是不會過的

以數據規模來看, 時間至少得壓在nlog(n)或O(n)
以nlog(n)去想的話, 代表我們可能得利用binary search去猜這個median然後再以O(n)時間驗證是不是可行
不然對於一連串的uniqueness來說, 如果不用猜而是去求出來的話, 不求出全部**n*(n+1)/2**也很難找出median

因此第一個想到的重點是: **試試binary search**

全部總共有`N = n*(n+1)/2`個median: [X X X X X X X X X X M X X X X X X X X X X], median = N/2

所以如果是利用bianry seawrch, 猜median uniqueness = mid的話
那麼題目就轉成去驗證這解是不是可行, 需要一個helper func `checkAtMost`去算有多少個**<=mid**的median個數.
也就是得找出median至多是`mid`的subarray個數有多少個

- if checkAtMost(mid) >= (N+1)/2: 代表我們median `mid`猜得太大. (注意奇數,偶數長度array的median位置 => [{X mid} X], [{X X mid} X] )
- if checkAtMost(mid) < (N+1)/2: 代表猜得太小, 且mid不會是中位數. => [{mid} X X]

binary search框架就能寫成:

```py
l, r = 1, n
while l < r:
    mid = l + (r-l)//2
    if checkAtMost(mid) >= (N+1)//2:
        r = mid
    else:
        l = mid+1
return l
```

那剩下就看如何實作出`checkAtMost(k)`這個helper function
這個要求的是: nums裡有多少個uniqueness(distinct number) <= k的subarray

我們可以利用sliding window去找出nums[l:r)之間distinct number <= k的位置
這樣對於左端點l來說, 右端點可以是[l:r)間的任意點, 所以組共有r-l個subarray

```py
def checkAtMost(nums, k):
    l = r = res = 0
    count = Counter()
    while r < n:
        count[nums[r]] += 1
        r += 1

        while l < r and len(count) > k:
            count[nums[l]] -= 1
            if count[nums[l]] == 0:
                del count[nums[l]]
            l += 1
        res += r-l
    return res
```

整理一下重點:

1. 得判斷出binary search這個方向, 去猜median of uniqueness
2. 再來得知道中位數性質, 利用總subarray數為N = n*(n+1)//2個這條件, 去驗證猜測的`mid` 這個是不是可行解
3. 所以目的就在於我們要找出有多少個subarray他至多有`mid`個unique number, 然後再去判斷:
   - 如果個數 >= (N+1)//2, 代表mid為可能解
   - 如果個數 < (N+1)//2, 代表mid猜得太小, 得排除