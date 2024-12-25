# Intuition - Pirority Queue

目標是找到max(values[i] + values[j] + i - j) = (values[i]+i + values[j]-j)

那我們可以遍歷nums[j]-j 然後利用max heap找出valid max (nums[i]+i)
然後valid nums[i] exists in values[:j]

time: O(nlogn)
space: O(n)

# Intuition - Dynamic Programming

再遍歷`values[j]-j`的過程中, 持續更新max left score (`values[i]+i`)