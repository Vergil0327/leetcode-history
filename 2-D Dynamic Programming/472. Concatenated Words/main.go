package main

import "fmt"

// https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
// GOD!!! elegant solution
func findAllConcatenatedWordsInADictOptimized(words []string) []string {

	dict := map[string]struct{}{}
	for _, word := range words {
		dict[word] = struct{}{}
	}

	var dfs func(s string) bool
	dfs = func(s string) bool {
		for i := 1; i < len(s); i++ {
			prefix, suffix := s[:i], s[i:]

			_, prefixOk := dict[prefix]
			_, suffixOk := dict[suffix]
			if prefixOk && suffixOk {
				return true
			}

			if prefixOk && dfs(suffix) {
				return true
			}

			if suffixOk && dfs(prefix) {
				return true
			}
		}

		return false
	}

	res := []string{}
	for _, word := range words {
		if dfs(word) {
			res = append(res, word)
		}
	}

	return res
}

// Best Solution
func findAllConcatenatedWordsInADictOptimizedMemo(words []string) []string {

	dict := map[string]struct{}{}
	for _, word := range words {
		dict[word] = struct{}{}
	}

	memo := map[string]bool{}

	var dfs func(s string) bool
	dfs = func(s string) bool {
		if _, ok := memo[s]; ok {
			return memo[s]
		}

		for i := 1; i < len(s); i++ {
			prefix, suffix := s[:i], s[i:]

			_, prefixOk := dict[prefix]
			_, suffixOk := dict[suffix]
			if prefixOk && suffixOk {
				return true
			}

			if prefixOk && dfs(suffix) {
				return true
			}

			if suffixOk && dfs(prefix) {
				return true
			}
		}

		memo[s] = false
		return false
	}

	res := []string{}
	for _, word := range words {
		if dfs(word) {
			res = append(res, word)
		}
	}

	return res
}

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
