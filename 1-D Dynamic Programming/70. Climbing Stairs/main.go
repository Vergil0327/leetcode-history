package main

// explanation:https://www.youtube.com/watch?v=Y0lT9Fck7qI
// 1, 2, ..., n-1, n
// ... ... ... one two pointer
func climbStairs(n int) int {
	one, two := 1, 1
	for i := 0; i < n-1; i++ {
		tmp := one
		one = one + two
		two = tmp
	}

	return one
}
