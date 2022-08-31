package main

import "strconv"

func hammingWeight(num uint32) int {
	bitExpr := strconv.FormatUint(uint64(num), 2)
	total := 0
	for _, ch := range bitExpr {
		if ch == '1' {
			total += 1
		}
	}

	return total
}

// T(n): O(32) = O(1) constant time because 32 bits totally
func hammingWeightBetter(num uint32) int {
	total := 0

	for num > 0 {
		lastBit := num % 2
		total += int(lastBit)
		num = num >> 1
	}

	return total
}

// Example.
// if n = 10000000001
// n &= n-1:
//   10000000001
// & 10000000000
// = 10000000000
// n &= n-1 again
//   10000000000
// & 01111111111
// = 00000000000
func hammingWeightTrick(num uint32) int {
	total := 0

	for num > 0 {
		num = num & (num - 1) // remove every first encountered '1' from the right side
		total += 1
	}

	return total
}
