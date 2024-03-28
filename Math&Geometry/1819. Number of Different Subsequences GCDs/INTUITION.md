# Intuition

Input: nums = [6,10,3]
Output: 5
Explanation: The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.

看到GCD, 首先先往質因數方向去想看看

```py
factors = [2*3  2*5  3]
```

1. 既然是subseq, 代表每個都能任選, 可選可不選
2. 然後duplicates沒有意義
3. 從constraint來看, 1 <= nums.length <= 10^5, 需要O(n), nlogn, 或頂多n * sqrt(nums), 找質因數的複雜度即為sqrt
4. 除掉duplicate, 至少有`n`種different GCD subsequence => 長度為1的subsequence
5. GCD只會隨著subseq.越長而越來越小

brute force的話, 2^n個subseq * O(n)的GCD計算

6. 由於nums[i] <= 2 * 10^5, 而GCD只會隨著subseq越長而越來越小, 或許我們可以遍歷每個可能GCD: [1, max(nums)], 然後找有沒有可能的組合來滿足該GCD?

這樣比起找出所有可能subseq. O(2^n)再去計算gcd, 時間複雜度會優秀許多
但前提是能高效確認能不能找出該GCD的subseq

```py
res = 0
for target_gcd in range(1, max(nums)+1):
    if check(target_gcd):
        res += 1
return res
```

接下來想要怎麼check(target): 目的是找到個subseqence的GCD**恰好**是target

我們可以找出所有包含target_gcd的倍數, 然後看他們的gcd是不是就是target
ex. gcd = 4

=> [4, 4*2, 4*3, 4*4, 4*5] => GCD = 4
=> [4*2, 4*4, 4*3] => GCD = 4
=> [4*2, 4*4] => GCD = 4*2 = 8

```py
def check(target):
    arr = [num for num in nums if num%target == 0]
    if not arr: return False

    GCD = arr[0]
    for num in arr:
        GCD = gcd(GCD, num)
    return GCD == target
```

那這樣整體複雜度就從遍歷所有subseq並計算gcd的O(2^n * n) 降為 O(n^2)
那麼, check的複雜度還能再往下降嗎?

比起遍歷整個nums, 感覺可以透過hashmap來預先處理一下來方便查找

對於每個nums[i]來說, 我們可以找出他的所有因數並作紀錄該因數有nums[i]

```py
def findFactors(num):
    facs = set()
    for x in range(1, int(sqrt(num))+1):
        if num%x == 0:
            facs.add(x)
            facs.add(num//x)
    return facs

factors = defaultdict(list)
for num in nums:
    for f in findFactors(num):
        factors[f].append(num)
```

那麼上面的`check`函式就能轉成:

```py
def check(target):
    arr = factors[target]
    if not arr: return False
    
    return reduce(lambda x, y: gcd(x, y), arr, arr[0]) == target
```

時間複雜度就能降到: O(n*sqrt(nums[i]) + n * factors.size) where factors.size = O(2 * sqrt(nums[i]))
所以整體時間複雜度就是O(n*sqrt(max(nums)))

但其實這時候會發現, 我們可以直接用hashmap存下GCD的結果即可, 這樣後續`check`只需要O(1)


# Optimized

同樣概念, 更簡潔的寫法則是:

```py
mx_num = max(nums)
seen = set(nums)

res = 0
for target_gcd in range(1, mx_num+1):
    gcd = 0
    for num in range(target_gcd, mx_num+1, target_gcd):
        if num in seen:
            gcd = math.gcd(gcd, num)
            if gcd == target_gcd:
                res += 1
                break
return res
```