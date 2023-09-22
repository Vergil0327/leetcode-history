# Intuition

首先看到求多少種方法以及要大數取餘, 先往dp方面去想

很直覺想到可以這麼設計dp:
`dp[i][num]: the number of special subsequences considering first i element and ended with num`

再來由於subseq. 結尾只可能是0, 1, 2
我們試著分情況討論

- Case 1: 當nums[i]為0時
  - 首先, 原本有多少個結尾為0的subseq. 就保底多少種方法`dp[i-1][0]`
  - 可加在所有結尾為0的subseq., 所以再多增加`dp[i-1][0]`種方法
  - 可自理門戶, 形成新的subseq., 再多1種方法

```
if nums[i] == 0:
    dp[i][0] += dp[i-1][0]*2+1 # 接在0後面 / 不接在0後面 / 自立門戶(new subseq.)
    dp[i][0] %= mod
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-1][2]
```

- Case 2: 當nums[i]為1時
  - 原本有多少個結尾為1的subseq. 就保底多少種方法`dp[i-1][1]`
  - 可加在所有結尾為1的subseq., 所以再多增加`dp[i-1][1]`種方法
  - 可接在結尾為0的subseq. 形成新的結尾為1的subseq

```
if nums[i] == 1:
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]*2 # 可接在結尾為0的subseq. / 加或不加在結尾1的subseq.
    dp[i][1] %= mod
    dp[i][2] = dp[i-1][2]
```

- Case 3:
  - 原本有多少個結尾為2的subseq. 就保底多少種方法`dp[i-1][2]`
  - 可加在所有結尾為2的subseq., 所以再多增加`dp[i-1][2]`種方法
  - 可接在結尾為1的subseq. 形成新的結尾為2的subseq
```
if nums[i] == 2:
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-1][1] + dp[i-1][2]*2 # 可接在結尾為1的subseq. / 加或不加在結尾為2的subseq
    dp[i][2] %= mod
```

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n*3)$$

# Concise Solution 2023/09/22

## Intuition

三種狀態
zero: the ways to form a subseq. ended at 0
one: the ways to form a subseq. ended at 1
two: the ways to form a subseq. ended at 2

0只能接在0後面, 或是自立門戶
zero只會從結尾是zero的狀態轉移過來或是單獨新開一個subseq.
zero += zero+1

1只能接在0或1後面
one只會從結尾是zero或one轉移過來
one += zero + one

2只能接在1或2後面
two只會從結尾是one或two轉移過來
two += one+two

```py
def countSpecialSubsequences(self, nums: List[int]) -> int:
    zero = one = two = 0
    for num in nums:
        if num == 0:
            zero += zero+1
            zero %= 1_000_000_007
        elif num == 1:
            one += zero + one
            one %= 1_000_000_007
        elif num == 2:
            two += one + two
            two %= 1_000_000_007
    return two
```