# Intuition

我們的操作是:
- 如果nums[i] == 0, 維持原方向
- 如果nums[i] > 0, 那就是`-= 1`然後換方向
這代表其實我們就是以`i`為基準, 左右兩方輪流`-= 1`


因此, 對於nums[i] == 0來說, 如果:
- sum(nums[:i]) == sum(nums[i+1:]): 這時不管選擇左右哪個方向, 都可以輪流扣除至0
- 如果兩方向和不相等, 不管選擇先走左邊或是右邊, 我們都只能輪流扣1, 只差在先走的那方向會比另方向多1次`-= 1`, 因此我們就看左右兩邊和是不是相差1即可

# Complexity

time: O(n)
space: O(n)

# Space-Optimized

遍歷過程中維護`left=sum(nums[:i])`跟`right=sum(nums[i+1:])`

```py
res = left = 0
right = sum(nums)
for i in range(n):
    right -= nums[i]
    
    # check abs(left-right) here

    left += nums[i]
return res

```