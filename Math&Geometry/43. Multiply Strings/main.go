// https://leetcode.com/problems/multiply-strings/
package main

import (
	"math"
	"strconv"
)

// explanation: https://www.youtube.com/watch?v=1vZswirL8Y8
func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	ans := make([]int, len(num1)+len(num2))

	for i := len(num1) - 1; i >= 0; i-- {
		for j := len(num2) - 1; j >= 0; j-- {
			idx := (len(num1) - 1 - i) + (len(num2) - 1 - j)
			digit := int(num1[i]-'0') * int(num2[j]-'0')
			ans[idx] += digit // might greater than 10
			carry := ans[idx] / 10
			ans[idx+1] += carry
			ans[idx] = ans[idx] % 10
		}
	}

	// because answer is reversed
	for i := 0; i < len(ans)/2; i++ {
		ans[i], ans[len(ans)-1-i] = ans[len(ans)-1-i], ans[i]
	}

	// remove leading zero
	i := 0
	for i < len(ans) && ans[i] == 0 {
		i += 1
	}
	ans = ans[i:]

	res := ""
	for _, v := range ans {
		res += strconv.Itoa(v)
	}
	return res
}

// !!! FAILED because integer will overflow
func multiplyFAILED(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	var ans int
	var carry int
	for i := len(num1) - 1; i >= 0; i-- {
		for j := len(num2) - 1; j >= 0; j-- {
			n1 := int(num1[i] - '0')
			n2 := int(num2[j] - '0')
			digit := n1 * n2

			ans += ((digit % 10) + carry) * int(math.Pow10(len(num2)-1-j+(len(num1)-1-i)))
			carry = digit / 10
		}
		ans += carry * int(math.Pow10(len(num2)+len(num1)-1-i))
		carry = 0
	}

	return strconv.Itoa(ans)
}
