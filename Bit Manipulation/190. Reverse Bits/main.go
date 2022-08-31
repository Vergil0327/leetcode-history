package main

import (
	"math"
)

// 00000000000000000000000000000001 -> 1000000000000000000000000000000
// 00000000000000000000000000000010 -> 0100000000000000000000000000000
// 00000000000000000000000000000100 -> 0010000000000000000000000000000
func reverseBits(num uint32) uint32 {
	var result uint32 = 0

	for i := 0; i < 32; i++ {
		lsb := num % 2
		power := 32 - float64(i) - 1
		if lsb != 0 {
			result += uint32(math.Pow(2, power))
		}
		num = num >> 1
	}
	return result
}

func reverseBitsBetter(num uint32) uint32 {
	var result uint32 = 0

	for i := 0; i < 32; i++ {
		// fmt.Println("result:", strconv.FormatUint(uint64(result), 2))
		result = result << 1
		if num%2 != 0 {
			result += 1
		}

		num = num >> 1
	}
	return result
}

func reverseBitsBest(num uint32) uint32 {
	var result uint32 = 0

	for i := 0; i < 32; i++ {
		bit := (num >> i) & 1               // get each bit from right to left
		result = result | (bit << (31 - i)) // push bit to the left & merge to result in bit representation
	}
	return result
}
