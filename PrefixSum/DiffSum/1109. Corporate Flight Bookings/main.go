package main

func corpFlightBookings(bookings [][]int, n int) []int {
	diff := make([]int, n)
	for _, booking := range bookings {
		// 1-based
		i, j, seats := booking[0], booking[1], booking[2]
		diff[i-1] += seats
		if j < n {
			diff[j] -= seats
		}
	}

	res := make([]int, n)
	res[0] = diff[0]
	for i := 1; i < n; i++ {
		res[i] = res[i-1] + diff[i]
	}
	return res
}
