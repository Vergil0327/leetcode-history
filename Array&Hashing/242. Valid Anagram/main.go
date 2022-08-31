package main

import (
	"fmt"
	"sort"
	"strings"
)

func isAnagramMap(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	m := map[rune]int{}
	for _, r := range s {
		m[r] += 1
	}

	for _, r := range t {
		if m[r] < 1 {
			return false
		}

		m[r] -= 1
	}

	for _, count := range m {
		if count != 0 {
			return false
		}
	}
	return true
}

func sortString(str string) string {
	s := strings.Split(str, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func isAnagramSort(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	return sortString(s) == sortString(t)
}

func isAnagramBest(s string, t string) bool {
	fingerprintS := [26]int{}
	for _, c := range s {
		fmt.Printf("%d, %d, c-'a':%d\n", c, 'a', c-'a')
		fingerprintS[c-'a']++
	}
	fingerprintT := [26]int{}
	for _, c := range t {
		fingerprintT[c-'a']++
	}

	fmt.Printf("fingerprintS:%+v\n", fingerprintS)
	fmt.Printf("fingerprintT:%+v\n", fingerprintT)
	return fingerprintS == fingerprintT
}
