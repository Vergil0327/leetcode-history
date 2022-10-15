package main

import "math"

// the most important thing is how to create `powers` array
// powers of 2 that sum to `n`:

// n = 1, `01` => powers = [1]
// n = 2, `10` => powers = [2]
// n = 3, `11` => powers = [1,2]
// ...

func productQueries(n int, queries [][]int) []int {
	var mod int = 7 + 1e9
	res := []int{}

	// The powers array can be created using the binary representation of n.
	powers := []int{}
	var x float64 = 0
	for n > 0 {
		if n&1 == 1 {
			powers = append(powers, int(math.Pow(2, x)))
		}
		x += 1
		n >>= 1
	}

	for _, q := range queries {
		l, r := q[0], q[1]

		ans := powers[r]
		for i := l; i < r; i++ {
			ans *= powers[i]
			ans %= mod
		}

		res = append(res, ans)
	}

	return res
}
