# Backtracking

## Intuition

由於數據範圍很小，因此可以嘗試用backtracking找出所有答案(python以外可通過)

我們要把`n`個數分成`k`個subset，因此每個subset size為`n//k`，並且每個subset不可有相同的nums[i]

先想這題一定有解嗎？
並不一定，如果有任何一個數的frequency大於k的話，我們將沒有辦法分出k個合法subset，因此我們可以先在一開始檢查

```py
counter = Counter(nums)
if any(freq > k for freq in counter.values()): return -1
```

再來就考慮要如何backtracking了

### step 1 
由於不可重複選取，我們可以先將nums排序
這樣我們一個一個選取nums[i]進入到當前subset後，下次就可以跳過重複nums[i]找出下一個nums[j]選入subset

因此一開始dfs框架會像是這樣

```py
nums.sort()
SUBSET_SIZE = n//k
visited = set()
def dfs(i, subsetSize):
    last = -1
    for j in range(i+1, n):
        if nums[j] == nums[i]: continue
        if last != -1 and nums[j] == last: continue
        if j in visited: continue
        
        visited.add(j)
        dfs(j, subsetSize+1)
        last = nums[j]
        visited.remove(j) # backtracking

visited.add(0)
dfs(0, 1)
```

那邊界條件當然就是當`當前的subset選滿的時候`，要重置條件，重新選出下個subset
等到`j`走到`n`時，代表我們已經選出`k`個subset了

```py
def dfs(i, subsetSize):
    if subsetSize == SUBSET_SIZE:
        j = 0
        while j < n and j in visited:
            j += 1
        
        if j == n:
            # do something
        else:
            visited.add(j)
            dfs(j, 1)
            visited.remove(j)
        return

    # ... see above    
```

由於incompatialty是subset裡的max-min，因此我們可以在backtracking過程中同時紀錄`min nums[i]`跟`max nums[i]`，並持續累加計算`incompatialty`

最後每當找完`k`個subset，就將最後`incompatialty`的累加結果更新到`res`上
最後返回res即可

# bistmask DP

## Intuition

第二種方法就是狀態壓縮DP
首先我們要從從n個nums[i]中，選出k個subset，每個subset的size為 `n//k`

因此可以想成一個n-bit的 `111...111` bitmask，分成k個有`n//k`個1的submask

要從n-bit bitmask中找出 m-1-bit submask的模板為:

```py
# Iterate all the n-bit state where there are m 1-bits.
state = (1<<m)-1
while state < (1<<n):
    # do something to submask

    c = state & -state # LSB
    r = state+c
    state = (((r^state)>>2)//c) | r
```

因此我們就能藉此找出所有subset，並同時計算他的imcompatialty
```py
states = []
values = []
subsetSize = n//k
state = (1<<subsetSize)-1
while state < (1<<n):
    hasDuplicate, incomp = containDuplicate(state)
    if not hasDuplicate:
        states.append(state)
        values.append(incomp)

    c = state & -state
    r = state+c
    state = (((r^state)>>2)//c) | r
```

**helper function: containDuplicate**

在`containDuplicate`要做的事就是
找出該state所對應的nums[i]
```py
values = []
for i in range(n):
    if (state>>i)&1:
        values.append(nums[i])
```

排序後如果有任意相鄰數相同，即為非法subset，如果合法，那麼該subset的incomaptialty則為:
max-min = values[-1] - values[0]

```py
values.sort()
for i in range(1, len(values)):
    if values[i] == values[i-1]:
        # found duplicate
incomaptialty = values[-1] - values[0]
```

在找出所有subset後，就是狀態壓縮的背包問題了

m = len(states)
總共`m`個state，定義dp[i][subset_state]為 the maximum incompatialty when considering first `i` states and subset state is `subset_state`

由於`i`只跟`i-1`有關，因此我們可以用兩個dp (dp, prevdp)來省空間，或是我們從後往前更新狀態，用一個dp同時代表dp及prevdp

在考慮前`i`個狀態，當前狀態是`state`
當我們考慮第`i`個state (states[i])時，如果states[i]是state的子集，代表我們可以從states[i]轉移到state
如果dp[state-states[i]]不是`inf`的話，那我們就可以轉移過去

狀態轉移為:
`dp[state] = min(dp[state], dp[state-states[i]] + values[i])`

```py
for i in range(m):
    for state in range(1<<n, -1, -1):
        if (state&states[i]) == states[i]:
            if dp[state-states[i]] != inf:
                dp[state] = min(dp[state], dp[state-states[i]]+values[i])
return dp[(1<<n)-1]
```

最終答案就是 `dp[111....1111]`，每個數都選到

## Optimzed

我們可以看到這步驟`for state in range(1<<n, -1, -1):`
要遍歷整個`1<<n`state，最高達$2^16$，這很有可能會TLE的

因此我們能預先處理，把不合法的狀態先挑掉

由於我們的狀態轉移，是從`n//k` size的subset轉移來的，因此`1-bit`必定是n倍的`n//k`

如果1不是`n//k`的倍數個，代表含有duplicate或是size不對

所以我們可以找出所有valid states然後替換掉第二層循環，這樣python就不會TLE了
```py
validStates = []
for state in range(1<<n):
    if bin(state).count("1") % subsetSize == 0:
        validStates.append(state)
```