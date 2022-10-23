package main

// Optimal Solution - Count GCD
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/discuss/2734442/Brute-Force-vs.-Count-GCDs
// nlog(max(nums))
func subarrayGCD(nums []int, k int) int {
	res := 0

	gcds := map[int]int{} // gcd: count
	for _, num := range nums {
		tmp := map[int]int{}
		if num%k == 0 {
			gcds[num] += 1
			for prevGcd, cnt := range gcds {
				tmp[gcd(prevGcd, num)] += cnt
			}
		}
		res += tmp[k]
		gcds, tmp = tmp, gcds
	}

	return res
}

func gcd(num1, num2 int) int {
	for num2 != 0 {
		num1, num2 = num2, num1%num2
	}
	return num1
}
