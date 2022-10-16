package main

import "strconv"

//     abcde
//     edcba
//     N-1 ... 0
//     (a+e)(b+d)(c+c)(d+b)(e+a)

//     443

// 169+961
// 170+071
// 171+171
// 172+271*
// 173+371
// I can't find any better solution, so let's brute force it
// luckily, constraints is small enough
func sumOfNumberAndReverse(num int) bool {
	for i := 0; i <= num; i++ {
		runes := []rune(strconv.Itoa(i))
		for l, r := 0, len(runes)-1; l < r; l, r = l+1, r-1 {
			runes[l], runes[r] = runes[r], runes[l]
		}
		revI, _ := strconv.Atoi(string(runes))
		if i+revI == num {
			return true
		}
	}
	return false
}
