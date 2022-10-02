package main

import (
	"math"
	"math/bits"
	"sort"
)

// https://leetcode.com/problems/minimize-xor/discuss/2648779/Java-Intuition-behind-logic-or-Minimize-XOR
func minimizeXorConcise(num1 int, num2 int) int {
	if num1 == num2 {
		return num1
	}

	bit := bits.OnesCount(uint(num2))

	res := 0
	for i := 31; i >= 0; i-- {
		currBit := (num1 >> i) & 1
		if currBit == 1 && bit > 0 {
			res |= (1 << i) // set i position
			bit -= 1
		}
	}

	// if bits to set are remaining, set the `LSB` least siginificant bit
	for i := 0; i < 32; i++ {
		// used all of the bit
		if bit == 0 {
			break
		}

		currBit := (res >> i) & 1
		if currBit != 1 {
			res |= (1 << i)
			bit -= 1
		}
	}

	return res
}

func minimizeXor(num1 int, num2 int) int {
	// find number of 1 bit
	count := 0
	num := num2
	for num > 0 {
		if num&1 == 1 {
			count += 1
		}
		num >>= 1
	}

	// x XOR num1 minimum -> x must remove num1 from most significant bit by XOR operation
	onePos := []int{}  // store position where bit is 1
	zeroPos := []int{} // store position where bit is 0
	pos := 0
	num = num1
	for num > 0 {
		if num&1 == 1 {
			onePos = append(onePos, pos)
		} else {
			zeroPos = append(zeroPos, pos)
		}

		pos += 1
		num >>= 1
	}

	// start from most significant bit to construct x
	sort.Sort(sort.Reverse(sort.IntSlice(onePos)))

	var x int
	maxBitPos := onePos[0] + 1

	for count > 0 && len(onePos) > 0 {
		v := onePos[0]
		x += int(math.Pow(2, float64(v)))

		count -= 1
		onePos = onePos[1:]
	}

	// If there are still bits to set, try to set them from the least significant bit
	for count > 0 && len(zeroPos) > 0 {
		v := zeroPos[0]
		zeroPos = zeroPos[1:]

		x += int(math.Pow(2, float64(v)))
		count -= 1
	}

	// If there are still bits to set, keep setting them to the left
	for count > 0 {
		x += int(math.Pow(2, float64(maxBitPos)))
		maxBitPos += 1
		count -= 1
	}

	return x
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
