# Intuition

對於nums[i]來說:
由於不用依序取, 假設最佳解的 nums[i] 是rotate j 次
即使nums[i-1]的最佳解是rotate j+1次, 我們仍可以在rotate j次的時候就先取走nums[i]
然後再rotate 1次取走nums[i-1]

所以我們可以試著從小到大嘗試每個rotation次數

- 並且如果rotate 0 次, 那麼nums[i] = nums[i]
- 如果已經rotate 1 次, 那麼nums[i] = nums[i] or nums[(i-1+n)%n]
  - 我們可以在rotate 0次的時候取走nums[i]
  - 也可以在rotate 1次的時候取走nums[i]
  - 我們可以在這兩種可能中挑最小的取走

- 如果已經rotate j 次, 那麼nums[i]就會經歷過nums[(i-rotation+n)%n]
  - 所以我們可以在0到j次rotation間, 任意時間點取走`min(nums[(i-rotation+n)%n])`

所以我們可以嘗試每個rotation
對於當前第 j 次rotation來說, nums[i]可以在[0,j]次rotation間任意時間點取走, 那我們當然取最小值
所以`minNum[i] = min(minNum[i], nums[(i-j+n)%n])` for 0 <= j < n
而這時的總cost為 sum(minNum[i])

我們取全局最小的總和即為答案
