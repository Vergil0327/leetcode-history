package main

// [a,b,c] [x,y,z]
// [a^x, a^y, a^z, b^x, b^y, b^z, c^x, c^y, c^z]
// a^x ^ a^y ^ a^z ^ b^x ^ b^y ^ b^z ^ c^x ^ c^y ^ c^z
// 交換律: a^a^a^b^b^b^c^c^c ^ x^x^x^y^y^y^z^z^z
// a^a == 0
// a^0 == a
// result := (a^b^c)^(x^y^z)

// T:O(n)
// M:O(1)
func xorAllNums(nums1 []int, nums2 []int) int {
	if len(nums1)&1 == 0 && len(nums2)&1 == 0 {
		return 0
	}

	// num in nums2 will repeat odd times
	if len(nums1)&1 == 1 && len(nums2)&1 == 0 {
		for i := 1; i < len(nums2); i++ {
			nums2[0] = nums2[0] ^ nums2[i]
		}
		return nums2[0]
	}

	// num in nums1 will repeat odd times
	if len(nums2)&1 == 1 && len(nums1)&1 == 0 {
		for i := 1; i < len(nums1); i++ {
			nums1[0] = nums1[0] ^ nums1[i]
		}
		return nums1[0]
	}

	for i := 1; i < len(nums1); i++ {
		nums1[0] ^= nums1[i]
	}
	for i := 1; i < len(nums2); i++ {
		nums2[0] ^= nums2[i]
	}
	return nums1[0] ^ nums2[0]
}

// https://leetcode.com/problems/bitwise-xor-of-all-pairings/discuss/2646552/JavaC%2B%2BPython-Easy-and-Concise
func xorAllNumsConcise(nums1 []int, nums2 []int) int {
	x, y := 0, 0
	for _, num := range nums1 {
		x ^= num
	}
	for _, num := range nums2 {
		y ^= num
	}
	return (len(nums1)%2)*x ^ (len(nums2) % 2) ^ y
}
