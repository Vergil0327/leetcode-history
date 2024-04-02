# Intuition

這題最初完全看不懂再問什麼
後來看解釋才發現他是在問:

我們能對groups進行任意排列, 並且我們每次都可以烤出`n * batchSize`個donuts
只要每個groups[i]的第一人拿到的是新鮮出爐的, 而非前個groups[i]拿完後剩下的, 那麼該groups就會happy
有就是當考察groups[i]時, 前面的人會剛好拿光所有donuts

所以我們將groups最個prefix sum的話

ex. groups = [6,2,4,5,1,3], batchSize=3
accumulate =  6 8 12 17 18 21
    index  =  1 2  3 4  5   6

會發現:
1. 第一組肯定是拿新鮮出爐的, 所以`happy+=1`
2. 第二組來的時候, 也是`happy+=1`, 因為前一組prefix sum = 6, 是batchSize的倍數, 烤出來的會剛好拿完
3. 第三組的時候前面總共會拿走`8`個, 由於是拿到remaining, 所以happy不變
4. 第四組時, prefix sum = 12, 代表前面總共會有12人拿走donuts, 也是batchSize的倍數, 所以這時第四組在拿的時候會是新鮮出爐的, `happy += 1`

因此他在問的是能有多少個: `accumulcate groups[i] % batchSize = 0`

brute force:

遍歷所有可能排列然後開始分配
第一組第一人肯定是拿到新鮮出爐, 因為當前donuts=0, donuts%batchSize=0, 所以happy += 1
並且會剩下: `donuts = (donuts + perm[0])%batchSize`
再來就繼續遍歷當前排列的groups[i], 然後看輪到i-th groups時, donuts%batchSize是不是為0即可知道當前拿到的是不是新鮮出爐的
所以:

```py
n = len(groups)
res = 0
for perm in permutations(groups, n):
    m = len(perm)
    happy = 0
    donuts = 0
    for i in range(m):
        if donuts%batchSize == 0:
            happy += 1
        donuts += perm[i]
        donuts %= batchSize

    res = max(res, happy)
return res
```

但這樣groups的全排列會有**30!**個, 這是個相當大的數字(2.6525286e+32)
所以我們再觀察一下, 我們真正關心的是donuts的`prefix sum % batchSize`

而1 <= batchSize <= 9, 所以`prefixSum % batchSize`最多只會有9種可能

因此, 我們可以先求出各個餘數的groups[i]數目有多少個

count[m]: 餘數為m的groups[i]有count[m]個

```py
count = [0]*batchSize
for num in groups:
    count[num%batchSize] += 1
```

那再來就是搜索所有可能

```py
def dfs(i, presum):
    if i == n: return 0

    res = 0
    for remainder in range(batchSize):
        if count[remainder] == 0: continue
        count[remainder] -= 1
        res = max(res, dfs(i+1, (presum+remainder)%batchSize))
        count[remainder] += 1
    return res + int(presum%batchSize == 0)
```

這麼做的好處是比起全排列, batchSize <= 9, 所以每次dfs搜索最多就9個選擇
時間複雜度為: 9^30
但即使如此, 所需時間還是很高, 所以我們還得配合memorization

所以我們得想辦法去對count做memorization

groups.length <= 30 => 所以count[i]最多就30, 我們可以用個5個bit來紀錄count[i]
batchSize <= 9, 所以最多有9種可能的count[i]
9 * 5 = 45 => 只需要45個bits即可紀錄count的資訊

所以這題其實可以轉化成bitmask + top-down dp

首先我們將count轉成bitmask:

首5個bits用來記錄餘數為0
第二組bits用來記錄餘數為1
...
直到紀錄完餘數為batchSize-1

```py
state = 0
for m in range(batchSize):
    state |= count[m] << (m*5)
```

那dfs就可改成:

```py
@cache
def dfs(i, presum, state):
    if i == len(groups): return 0

    happy = 0
    for remainder in range(batchSize):
        count = (state >> (remainder*5))%(1<<5)
        if count == 0: continue
        
        state -= 1<<(remainder*5)
        happy = max(happy, dfs(i+1, (presum+remainder)%batchSize))
        state += 1<<(remainder*5)
    return happy + int(presum%batchSize == 0)
```

[推薦詳解說明 by @HuifengGuan](https://www.youtube.com/watch?v=DDCl7TcrkDc&ab_channel=HuifengGuan)