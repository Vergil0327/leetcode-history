package main

/*
Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:
Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
*/

// T:O(logn), M:O(1)
func missingElementByIndex(nums []int, k int) int {
	l, r := 0, len(nums)
	for l < r {
		mid := l + (r-l)/2
		if missingEl(nums, mid) < k {
			l = mid + 1
		} else {
			r = mid
		}
	}

	// l is upperbound, missing elements <= k
	// nums[l-1], missing element < k
	// our target is nums[l-1] + distance of target missing elements
	// => nums[l-1] + k-(missing elements before l-1)
	return nums[l-1] + (k - missingEl(nums, l-1))
}

// 4,5,8,9,10, index=2 -> nums[2]-nums[0]-index = 8-4-2=2
// missing element = 2 because if no missing element, nums[index]-nums[0] should equal its index
func missingEl(nums []int, index int) int {
	return nums[index] - nums[0] - index
}

// search space: values
// T:O(nlogn)
// M:O(n)
func missingElement(nums []int, k int) int {
	l, r := nums[0], nums[len(nums)-1]+k
	m := map[int]bool{}
	for _, num := range nums {
		m[num] = true
	}

	for l <= r {
		mid := l + (r-l)/2

		missing := []int{}
		for i := nums[0]; i <= mid; i++ {
			if _, ok := m[i]; !ok {
				missing = append(missing, i)
			}
		}

		if len(missing) == k {
			return missing[len(missing)-1]
		} else if len(missing) > k {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return -1
}
