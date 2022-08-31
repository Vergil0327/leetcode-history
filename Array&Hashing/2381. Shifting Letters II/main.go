// https://leetcode.com/contest/biweekly-contest-85/problems/shifting-letters-ii/
package main

import "strings"

func shiftingLetters(s string, shifts [][]int) string {
	delta := make([]rune, len(s)+1)
	for _, shift := range shifts {
		start, end, dir := shift[0], shift[1], shift[2]
		if dir == 1 {
			delta[start] += 1
			delta[end+1] -= 1
		} else {
			delta[start] -= 1
			delta[end+1] += 1
		}
	}

	// nice technique to prevent for-loop nested above to fill the delta
	// it's called "prefix sum"
	// https://blog.csdn.net/ch_609583349/article/details/106423315
	for i := 1; i < len(s)+1; i++ {
		delta[i] += delta[i-1]
	}

	var offset = rune(26)
	arr := make([]string, len(s))
	for i, letter := range s {
		ch := (letter-'a'+delta[i])%offset + 'a'
		if ch < 'a' {
			ch += offset
		}
		arr = append(arr, string(ch))
		// fmt.Printf("[%d]%s --> %d --> %s\n", i, string(letter), delta[i], string(ch))
	}

	return strings.Join(arr, "")
}

func shiftingLettersTIMEOUT(s string, shifts [][]int) string {
	arr := make([]rune, len(s))
	for i, r := range s {
		arr[i] = r
	}

	var offset = 'z' - 'a' + 1
	for _, shift := range shifts {
		start, from, dir := shift[0], shift[1], shift[2]
		for i := range arr[start : from+1] {
			if dir == 1 {
				arr[start+i] = arr[start+i] + 1
				if arr[start+i] > 'z' {
					arr[start+i] = arr[start+i] - offset
				}
			} else {
				arr[start+i] = arr[start+i] - 1
				if arr[start+i] < 'a' {
					arr[start+i] = arr[start+i] + offset
				}
			}
		}
	}

	res := ""
	for _, v := range arr {
		res += string(v)
	}
	return res
}
