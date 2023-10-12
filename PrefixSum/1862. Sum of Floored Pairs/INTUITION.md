# intuition

先隨便亂想能想到的是:
只關注pair -> 先看看排序有沒有幫助sum(nums[i]/nums[j])
由於可能會有重複, 避免重複計算可以用個hashmap來計數
hashmap[nums[i]] = freq

對於nums[i]來說, 所有大於nums[i]的nums[j]都會得到０, 所以可以不考慮
對於nums[i]來說只需考慮nums[0:i]

也可反過來看說, 對於nums[j]而言:
- 如果`round(nums[i]/nums[j]) = k`
- 位於[nums[j]*k, nums[j]*(k+1)-1]之間的nums[i], round(nums[i]/nums[j])都是k

所以會發生一個區段一個區段的round(nums[i]/nums[j])都是一樣的
因此對於nums[j]而言, 他所貢獻的sum就是每個區間和加起來

所以如果:
- count[nums[j]*k] = a
- count[nums[j]*(k+1)-1] = b
那麼[a,b]這段區間和就能得知有幾個nums[i], 然後再乘上k就是nums[j]所貢獻的round(nums[i]/nums[j])
由於`nums[j]*(k+1)-1 <= nums[-1]`, k的上限就是 k <= ((nums[-1]+1)/nums[j])-1

所以我們的做法是
我們先求出:
- count[num]
- presum[num]
- remove duplicate: set(nums)

前兩項:
```py
nums.sort()
N = nums[-1]

count = [0] * (N+1)
for num in nums:
    count[num] += 1

presum = [0] * (N+1)
for i in range(1, N+1):
    presum[i] = presum[i-1] + count[i]
```

再來就遍歷不重複的nums[j], 然後在遍歷k
由於`nums[j]*(k+1)-1 <= nums[-1]`, k的上限就是 k <= ((nums[-1]+1)/nums[j])-1
我們向上取整數, 然後presum記得避免越界, 加上個min(nums[-1])
這樣我們遍歷k就能得到各個區間和為:
```py
ans += k * (presum[min(nums[-1], numj*(k+1)-1)] - presum[numj*k-1]) % mod
```
最後ans就是nums[j]的貢獻和, see example 2, 由於可能有duplicate, 所以這個貢獻還得乘上個數
```py
res = (res + ans*count[numj])%mod
```

```py
res = 0
for numj in set(nums):
    ans = 0
    for k in range(1, ceil(((nums[-1]+1)/numj)-1)+1):
        ans += k * (presum[min(nums[-1], numj*(k+1)-1)] - presum[numj*k-1]) % mod
        ans %= mod

    res = (res + ans*count[num])%mod
return res
```

時間複雜度分析
這邊雖然是兩個loop, 但由於k受限於nums[i]/nums[j]
當nums[j]越小, 遍歷的區間`k`就越多
當nums[j]逐漸增大, k會越來越小
所以這邊會是個log級別的時間複雜度
再加上透過set(nums)避免重複運算, 所以時間上會優於brute force: O(n^2)