package main

import "strings"

func wordBreak(s string, wordDict []string) []string {
	res := map[string]bool{}

	var dfs func(state strings.Builder, str string)
	dfs = func(state strings.Builder, str string) {
		if res[state.String()] {
			return
		}

		if str == "" {
			res[state.String()] = true
			return
		}

		for _, word := range wordDict {
			// make sure index in bounds
			if idx := min(len(str), len(word)); str[:idx] == word {
				newStr := strings.Builder{}
				newStr.WriteString(state.String())
				newStr.WriteString(word)
				if idx != len(str) { // we don't need to append space in the last
					newStr.WriteString(" ")
				}
				dfs(newStr, str[len(word):])
			}
		}
	}
	dfs(strings.Builder{}, s)

	strs := []string{}
	for str := range res {
		strs = append(strs, str)
	}
	return strs
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
