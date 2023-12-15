# Intuition

返回一個[1,n]的數列, 並且其中對於任意兩個`i`, `j`位置, 不存在一個`k`使得:
`2 * nums[k] == nums[i] + nums[j]` => `nums[k] == (nums[i]+nums[j])/2`

代表每個nums[k]不可放在nums[k]-n, nums[k]+n之間
=> 任意兩數的平均不可放在他們兩數之間

所以:
1. 如果nums[i]+nums[j]為奇數, 那們兩數可任意擺放
2. 如果nums[i]+nums[j]為偶數, 那們他們倆的平均不可放置在他們兩數之間

再來
根據上面第一點提到的, 奇數跟偶數相加為奇數, 兩者任意擺放, 中間必定不會有不合法的數值存在
所以如果有個都是奇數的beautiful array以及一個都是偶數的beautiful array的話
兩邊的數任意配對都不會存在一個合法的nums[k]整數
所以兩者拼再一起, 必定也是個合法的beautiful array

因此將[1,n]範圍拆成奇數跟偶數兩array, [奇數...][偶數...]
然後再將兩邊奇數偶數個別組成beautiful array後
再拼接起來便是一個範圍[1,n]的合法的beautiful array

那該如何從一個範圍[1,n]的數組出beautiful odd/even array?

如果我們已經有個beautiful array了, 我們對
- 每個數 *2 => 依舊是beautiful array, 因為`nums[k] == (nums[i]+nums[j])/2`依舊成立
- 每個數 -1 => 依舊是beautiful array, 因為`nums[k]-1 == (nums[i]-1+nums[j]-1)/2`依舊成立

所以我們從n=1的beautiful array開始:
- 奇數beautiful array => 對原本beautiful array每個數`*2-1`轉為奇數
- 偶數beautufuil array => 對原本beautiful array每個數`*2`轉為偶數
- 再配合上面討論的, 將奇數beautiful arr跟偶數beautiful arr拼接起來, 依舊beautiful
最終就會得到符合長度或超過長度的beautiful array了, 最終記得把不合法的數filter掉即可

time: O(nlogn)

另外也能用recursion+memorization達到O(n)