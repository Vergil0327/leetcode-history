// https://leetcode.com/problems/reverse-words-in-a-string-ii/
package main

import "fmt"

/* Follow up: Could you do it in-place without allocating extra space? */

/* Do not return anything, modify s in-place instead */
func reverseWords(s []string) {
	/*
		Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
							e		u		l		b		""	s		i		""	y		k		s		""	e	 	h		t
		Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
	*/
	for l, r := 0, len(s)-1; l < r; l, r = l+1, r-1 {
		s[l], s[r] = s[r], s[l]
	}

	prevStop := 0
	stop := 0
	for stop < len(s) {
		for stop < len(s) && s[stop] != " " {
			stop += 1
		}

		for l, r := prevStop, stop-1; l < r; l, r = l+1, r-1 {
			s[l], s[r] = s[r], s[l]
		}
		stop += 1
		prevStop = stop
	}
}

// https://www.cnblogs.com/grandyang/p/5186294.html
// 先把每個單詞翻轉一遍，再把整個字符串翻轉一遍，或者也可以調換個順序，先翻轉整個字符串，再翻轉每個單詞
func reverseWordsOptimized(s []string) {
	left := 0
	for i := left; i <= len(s); i++ {
		if i == len(s) || s[i] == " " {
			reverse(&s, left, i-1)
			left = i + 1
		}
	}

	reverse(&s, 0, len(s)-1)
	fmt.Println(s)
}
func reverse(s *[]string, l, r int) {
	for i, j := l, r; i < j; i, j = i+1, j-1 {
		(*s)[i], (*s)[j] = (*s)[j], (*s)[i]
	}
}

// T:O(n) M:O(n)
func reverseWordsWithSpace(s []string) []string {
	group := [][]string{}
	word := []string{}
	for _, str := range s {
		if str != " " {
			word = append(word, str)
		} else {
			group = append(group, word)
			word = make([]string, 0)
		}
	}
	group = append(group, word)

	for i, j := 0, len(group)-1; i < j; i, j = i+1, j-1 {
		group[i], group[j] = group[j], group[i]
	}

	offset := 0
	for i := 0; i < len(group); i++ {
		for j := 0; j < len(group[i]); j++ {
			s[j+offset] = group[i][j]
			if i != len(group)-1 && j == len(group[i])-1 {
				offset += 1
				s[j+offset] = " "
			}
		}
		offset += len(group[i])
	}

	return s
}
