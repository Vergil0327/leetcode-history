# Intuition

遇到要求 arr[i] ,arr[j], arr[k] 三個組合的合法數目時
首先該直覺想到的是我們可以遍歷中間，然後找左右兩個

這裡我們對arr做**排序**，然後限制`i<j<k`，這樣我們就不會挑到重複
所以首先外層循環我們遍歷中間的`j`, 範圍從[1,n-1]
然後我們用two pointers `i`, `k`來找出合法的 arr[i] + arr[j] + arr[k] == target
內層循環就是移動左邊的`i`，然後透過`arr[k] == target-arr[i]-arr[j]`來找出k

 [X X] X X X X X X [X X X] X X X X X
    i      j        k           <- k

首先我們先找出arr[i]有多少個duplicate
```py
# count duplicate
countI = 1
while i+1 < j and arr[i] == arr[i+1]:
    countI += 1
    i += 1
```

然後我們開始移動k找合法的arr[k]

1. 首先先移動不合法的arr[k], 排除掉 arr[k] > target-arr[i]-arr[j]:
```py
while j < k and arr[k] > target-arr[i]-arr[j]:
    k -= 1
```

2. 跳出循環後再看合法的k有多少個
```py
while j < k and arr[k] == target-arr[i]-arr[j]:
    countK += 1
    k -= 1
```

所以此時以nums[j]作為中間數的合法可能組合有`countI * countK`個
最後答案就是這些可能組合數的加總

# Optimized

另外有種更高效的方法是透過每個數出現的frequency來透過數學求解
先算出每個數出現多少次，然後不重複的遍歷`i`
找出nums[i]後, 也就可以找出相對應的nums[j], nums[k]使得`target-nums[i] == nums[j] + nums[k]`

一樣透過雙指針移動j, k 並且`j, k = i, n-1`

如果 nums[j] + nums[k] > target-nums[i], 就移動k
如果 nums[j] + nums[k] < target-nums[i], 就移動j
如果nums[j] + nums[k] == target-nums[i], 那就探討以下幾種情況:
1. i < j < k: 代表三種數都不相同，方法數就是他們各自的的freq相乘
2. i == j < k: 如果是nums[i]等於nums[j]的情況, 如果nums[i]有M個，那就是組合數C M 取 2個組合乘上 nums[k]的freq
3. i < j == k: 同理, nums[j] == nums[k]的話，那就是算從nums[j]的所有個數中取出2個的組合數乘上nums[i]的個數
4. i == j == k: 那就是 C counter[nums[i]] 取 3
```py
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = int(1e9+7)
        counter = Counter(arr)
        nums = sorted(list(counter.keys()))
        n = len(nums)
        
        res = 0
        for i, num in enumerate(nums):
            j = i
            k = n-1
            SUM = target-num
            while j <= k:
                currSUM = nums[j] + nums[k]
                if currSUM > SUM:
                    k -= 1
                elif currSUM < SUM:
                    j += 1
                else:
                    if i < j < k:
                        res += counter[nums[i]] * counter[nums[j]] * counter[nums[k]]
                        res %= MOD
                    elif i == j < k:
                        # C counter[nums[i]] 取 2
                        res += math.comb(counter[nums[i]], 2) * counter[nums[k]]
                        res %= MOD
                    elif i < j == k:
                        res += counter[nums[i]] * math.comb(counter[nums[k]], 2)
                        res %= MOD
                    else: # i == j == k
                        res += math.comb(counter[nums[j]], 3)
                        res %= MOD
                    j, k = j+1, k-1
        return res
```