# Intuition

我們要找一個subset，其中他們的乘積不被任何不為1的平方數整除
我們可看到nums[i] <= 30，代表這個subset的乘積必定是小於等於30的質因數的乘積所組成，並且每個質因數最多只能有一個

*因為只要有大於1個的質因數，代表存在一個平方數*

首先我們可以很快的找出小於等於30的質因數有:

`primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

可以看到就只有這**10**個質因數存在，因此所有合法解必定是他們的subset乘積，因此我們可以用二進位bitmask來表示，最多就1<<10，1024種

ex.
如果nums[i] = 3 我們可以用bitmask `10`來表示
代表他用到了primes[1]

ex.
如果nums[i] = 15 = 3*5，我們可以用bitmask`110`來表示
代表他是primes[1]跟primes[2]的乘積

所以再來我們可以把不合法的`nums[i]`剔除掉，並且把合法的`nums[i]`用bitmask表示

由於nums[i] <= 30，但nums.length <= 1000
代表裡面存在著很多重複的數，所以我們首先先找出他們的counter:
`countNums = Counter(nums)`

那如果nums[i]可以被primes[j]整除的話，並且不能被第二次整除的話，代表他不包含平方數，所以可以加到validStates裡

>至於nums[i] = 1這個edge case我們先排除掉

```py
countNums = Counter(nums)

counter = defaultdict(int)
validStates = []
for num, cnt in countNums.items():
    if num == 1: continue # edge case

    invalid = False
    bit = 0
    for i, p in enumerate(primes):
        if num%p == 0:
            bit |= (1<<i)
            num //= p
            if num % p == 0:
                invalid = True
                break
    if invalid: continue
    
    validStates.append(bit)
    counter[bit] = cnt
```

在找到所有合法validStates後再來就是背包問題了
遞歸方式的話很簡單

每個validStates[i]可選可不選
如果不選，那就是:
`res = dfs(i+1, bitmask)%MOD`

如果要選，那就要看一下bitmask，
當前的bitmask表示我們的選擇狀態，如果`if bitmask & validStates[i] == 0`，代表我們可以選擇validStates[i]

有多少個validStates[i]就有多少種subset，所以我們加上`1 * counter[validStates[i]]`這麼多種

```py
n = len(validStates)
@lru_cache(None)
def dfs(i, bitmask):
    if i == n: return 1

    res = dfs(i+1, bitmask)%MOD
    if bitmask & validStates[i] == 0:
        res += dfs(i+1, bitmask | validStates[i]) * counter[validStates[i]]
    return res%MOD
```

那最後再來考慮edge case `validStates[i]為1`的情形

如果我們有`n`個1，代表我們會額外多出`2^n`種方法
因為每個1加或不加都會是合法subset，所以如果有`n`個1就代表有`2^n`種加法，所以我們最終結果還得乘上`2**countNums[1]`

所以我們總共有`dfs(0, 0)*(2**countNums[1])`這麼多種的subset

由於題目說必須不能為空的subset，所以減去1就是答案