package leetcode_2575

import "strconv"

func divisibilityArray(word string, m int) []int {
	res := []int{}
	n := len(word)
	num := 0
	for i := 0; i < n; i++ {
		v, _ := strconv.Atoi(string(word[i]))
		num = (num*10 + v) % m
		if num == 0 {
			res = append(res, 1)
		} else {
			res = append(res, 0)
		}
	}
	return res
}
