package main

import "fmt"

// Runtime: 3714 ms, faster than 7.14% of Go online submissions for Concatenated Words.
// Memory Usage: 7 MB, less than 90.48% of Go online submissions for Concatenated Words.
func findAllConcatenatedWordsInADict(words []string) []string {
	memo := map[string]bool{} // "word,count": bool

	var dfs func(s string, count int) bool
	dfs = func(s string, count int) bool {
		key := fmt.Sprintf("%s,%d", s, count)

		if s == "" {
			if count <= 0 {
				return true
			}

			memo[key] = false
			return false
		}

		if _, ok := memo[key]; ok {
			return memo[key]
		}

		for _, word := range words {
			// prune impossible candidates
			if len(word) > len(s) {
				continue
			}

			// prefix must be concatenated by one of words
			if s[:len(word)] == word {
				if dfs(s[len(word):], count-1) {
					return true
				}
			}
		}

		memo[key] = false
		return false
	}

	candidates := map[string]struct{}{}
	for _, word := range words {
		// try all the word and concatenated 2 shorter word at least
		if dfs(word, 2) {
			candidates[word] = struct{}{}
		}
	}

	res := []string{}
	for candidate := range candidates {
		res = append(res, candidate)
	}

	return res
}
