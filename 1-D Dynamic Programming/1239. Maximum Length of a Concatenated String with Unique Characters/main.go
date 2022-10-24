package main

import (
	"fmt"
)

func maxLengthMask(arr []string) int {
	uniqMasks := []uint32{}
	for _, s := range arr {
		if mask, ok := getMask(s); ok {
			uniqMasks = append(uniqMasks, mask)
		}
	}

	var dfs func(state uint32, i int) int
	dfs = func(state uint32, i int) int {
		if i == len(uniqMasks) {
			return countOnes(state)
		}

		longest := countOnes(state)
		for j := i; j < len(uniqMasks); j++ {
			if state&uniqMasks[j] != 0 { // overlapping, has duplicate
				continue
			}

			longest = max(longest, dfs(state|uniqMasks[j], j+1))
		}

		return longest
	}

	return dfs(0, 0)
}

func countOnes(mask uint32) int {
	count := 0
	for i := 0; i < 32; i++ {
		if mask&(1<<i) != 0 {
			count += 1
		}
	}

	return count
}

func getMask(word string) (mask uint32, ok bool) {
	for _, c := range word {
		if mask&(1<<(c-'a')) != 0 { // repeated characters
			return 0, false
		}
		mask |= 1 << (c - 'a')
	}
	return mask, true
}

func maxLength(arr []string) int {
	uniq := []string{}

	// prune invalid result
	for _, s := range arr {
		if checkUniq(s) {
			uniq = append(uniq, s)
		}
	}

	memo := map[string]int{}
	var dfs func(state string, i int) int
	dfs = func(state string, i int) int {
		if i == len(uniq) {
			return 0
		}

		key := fmt.Sprintf("%s,%d", state, i)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		longest := 0
		for j := i; j < len(uniq); j++ {
			str := uniq[j]
			if hasDuplicate(state, str) {
				continue
			}

			longest = max(longest, len(str)+dfs(state+str, j+1))
		}

		memo[key] = longest
		return longest
	}

	return dfs("", 0)
}

func checkUniq(s string) bool {
	seen := map[rune]struct{}{}
	for _, c := range s {
		if _, ok := seen[c]; ok {
			return false
		}

		seen[c] = struct{}{}
	}
	return true
}

func hasDuplicate(state, str string) bool {
	has := map[rune]struct{}{}
	for _, c := range state {
		has[c] = struct{}{}
	}

	for _, c := range str {
		if _, ok := has[c]; ok {
			return true
		}
	}
	return false
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
