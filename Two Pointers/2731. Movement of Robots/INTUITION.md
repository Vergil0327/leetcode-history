# Intuition
相撞後馬上轉方向:
A -> <- B => [<-A,B->] => <- A [] B -> 

因為最後(A, B) pair跟(B,A) pair是一樣的
所以A, B兩者互換後
其實就相當於A, B沒有碰撞: <-B [] A->
所以其實就看每個位置在d秒後的位置在哪
然後計算每個pair的距離並加總即可

那計算一個橫軸上任一兩點的距離和我們可以這麼來看
[-3,-1,1,2,5] -> 排序後的結果
(-3,5) == (-3,-1) + (-1,5) == (-3,1) + (1,5) == (-3,2) + (2,5)
(-1,2) == (-1,1) + (1,2)
我們可發現一整段的距離可拆成兩段距離和, 也就是兩個pair的距離和
-3可以跟-1, 1, 2, 5配對
同樣的當-3跟-1配對時, -1可跟-5配對, 這時的距離又等同於(-3,-5)
觀察後我們可以用雙指針來計算每個pair的距離和為
(nums[r] - nums[l]) * pair 數

# Other Solution

但其實計算任兩點的距離和也可以用prefix sum

首先對於nums[i]來說, 他
`abs(num[0]-nums[i]) + abs(nums[1]-nums[i]) + ... ＋ abs(nums[i-1]-nums[i])`

當我們一樣對array排序後拿掉abs()就等於
```
=> nums[i]-nums[0] + nums[i]-nums[1] + ... + nums[i]-nums[i-1]
=> i * nums[i] - sum(nums[0] + sum[1] + ... + nums[i-1])
=> i * nums[i] - prefix_sum[0:i-1]
```

所以最後計算為:
```py
res = 0
presum = [0] + list(accumulate(nums))
for i in range(1, n):
    res += i * nums[i] - presum[i]
    res %= mod
return res
```