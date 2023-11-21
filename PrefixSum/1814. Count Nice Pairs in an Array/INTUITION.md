# Intuition

nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
=> nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
=> find X and previous Y such that X == Y

create an array `arr` which arr[i] = nums[i] - rev(nums[i])
then iterate i and use hashmap to store previous j such that hashmap[arr[j]] = count

use prefix sum + hashmap to count nice pairs

time: $O(n)$
space: $O(n)$