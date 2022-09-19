// https://leetcode.com/problems/4sum-ii/
package main

// T:O(n^2)
// https://leetcode.com/problems/4sum-ii/discuss/1740606/Going-from-O(N4)-greater-O(N3)-greater-O(N2)-JavaC%2B%2B
func fourSumCountOptimized(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	m12 := map[int]int{} // [sum,count]
	for i := range nums1 {
		for j := range nums2 {
			m12[nums1[i]+nums2[j]] += 1
		}
	}

	count := 0
	for k := range nums3 {
		for l := range nums4 {
			sum34 := nums3[k] + nums4[l]
			count += m12[-sum34]
		}
	}

	return count
}

// extend TwoSum technique, two hashmap
// T:O(n^2)
func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	m12 := map[int]int{} // [sum,count]
	for i := range nums1 {
		for j := range nums2 {
			m12[nums1[i]+nums2[j]] += 1
		}
	}
	m34 := map[int]int{} // [sum,count]
	for k := range nums3 {
		for l := range nums4 {
			m34[nums3[k]+nums4[l]] += 1
		}
	}

	count := 0
	for sum, cnt1 := range m12 {
		if cnt2, ok := m34[-sum]; ok {
			count += cnt1 * cnt2
		}
	}

	return count
}

// TwoSum
// T:O(n^3)
func fourSumCountTLE(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	m34 := map[int]int{} // [sum,count]
	for k := range nums3 {
		for l := range nums4 {
			m34[nums3[k]+nums4[l]] += 1
		}
	}

	count := 0
	for i := range nums1 {
		for j := range nums2 {
			for subSum, cnt := range m34 {
				if sum := nums1[i] + nums2[j] + subSum; sum == 0 {
					count += cnt
				}
			}
		}
	}

	return count
}

// T:O(n^4)
func fourSumCountBruteForce(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	count := 0
	for i := range nums1 {
		for j := range nums2 {
			for k := range nums3 {
				for l := range nums4 {
					sum := nums1[i] + nums2[j] + nums3[k] + nums4[l]
					if sum == 0 {
						count += 1
					}
				}
			}
		}
	}

	return count
}
