// https://leetcode.com/problems/largest-palindromic-number/
package main

import (
	"strconv"
	"strings"
)

func largestPalindromic(num string) string {
	count := map[int]int{}
	for _, str := range num {
		v, _ := strconv.Atoi(string(str))
		count[v] += 1
	}

	res := []string{}
	center := -1

	for i := 9; i >= 0; i-- {
		if _, ok := count[i]; !ok {
			continue
		}

		if count[i]%2 != 0 {
			if i > center {
				center = i
			}
		}

		// make sure no leading zeros
		if i == 0 && len(res) == 0 {
			continue
		}

		for count[i] > 1 {
			res = append(res, strconv.Itoa(i))
			count[i] -= 2
		}
	}

	if len(res) == 0 && center == -1 {
		return "0"
	}

	length := len(res)

	// !!! check existence of center
	if center != -1 {
		res = append(res, strconv.Itoa(center))
	}

	for i := length - 1; i >= 0; i-- {
		res = append(res, res[i])
	}

	return strings.Join(res, "")
}
