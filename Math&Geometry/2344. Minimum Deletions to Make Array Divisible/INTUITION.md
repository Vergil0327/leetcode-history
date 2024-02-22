# Intuition

we want smallest element in nums which divides all numsDivide, 直覺想到
1. nums可以先排序, 方便查找smallest element
2. numsDivide可先去除重複的數
        
all numsDivide % min(nums) == 0
=> if nums[i] <= numsDivide[j], numsDivide[j]必須至少有nums[i]的所有因數個數
=> if nums[i] > numsDivide[j], numsDivide[j] % nums[i] = nums[i] != 0 => **invalid**
=> min(nums) 是 numsDivide的公因數

既然如此, 那我們找出numsDivide整個的最大公因數 `x`
如果最大就x, 那合法的nums[i]肯定是x的因數
所以如果`x%nums[i] == 0`代表nums[i]能整除每個numsDivide[j], 這時我們就返回i即可


time: O(nlogn) where n = nums.length
space: O(1)