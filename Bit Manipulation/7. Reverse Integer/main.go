// https://leetcode.com/problems/reverse-integer/
package main

import (
	"fmt"
	"math"
	"strconv"
)

// explanation: https://www.youtube.com/watch?v=HAgLH58IgJQ
// Time Complexity: O(log(x)). There are roughly log10(x) digits in xx.
// Space Complexity: O(1)
func reverse(x int) int {
	MAX, MIN := math.MaxInt32, math.MinInt32

	ans := 0
	for x > 0 {
		digit := x % 10
		x /= 10

		// check if we're gonna overflow
		// positive constraint
		if ans > MAX/10 || (ans == MAX/10 && digit > MAX%10) {
			return 0
		}

		// negative constraint
		if ans < MIN/10 || (ans == MIN/10 && digit < MIN%10) {
			return 0
		}

		ans = ans*10 + digit
	}

	return ans
}

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
// Time Complexity: O(log(x)). There are roughly log10(x) digits in xx.
// Space Complexity: O(log(x))
func reverseByArray(x int) int {
	constraint := int32(math.Pow(2, 31) - 1)

	isPositive := x > 0
	xAbs := int(math.Abs(float64(x)))

	digits := []int{}
	for xAbs != 0 {
		digit := xAbs % 10
		digits = append(digits, digit)
		xAbs /= 10
	}

	ans := 0
	for len(digits) > 0 {
		length := len(digits)
		digit := digits[0]
		digits = digits[1:]

		if (int(constraint) - ans) < digit*int(math.Pow10(length-1)) {
			return 0
		}

		ans += digit * int(math.Pow10(length-1))
	}

	if isPositive {
		return ans
	}
	return -ans
}

// ! Can't do this because we've already overflow
// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
func reverseByFmt(x int) int {
	isPositive := x > 0
	str := []rune(fmt.Sprintf("%d", int(math.Abs(float64(x)))))
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		str[i], str[j] = str[j], str[i]
	}

	digit, _ := strconv.Atoi(string(str))
	if isPositive {
		if digit > int(math.Pow(2, 31)) {
			return 0
		}
		return digit
	} else {
		if -digit < -int(math.Pow(2, 31)) {
			return 0
		}
		return -digit
	}
}
