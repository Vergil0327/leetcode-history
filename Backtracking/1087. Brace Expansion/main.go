package main

import (
	"sort"
	"strings"
)

func expand(s string) []string {
	if s == "" {
		return nil
	}

	res := []string{}
	var dfs func(state []string, i int)
	dfs = func(state []string, i int) {
		if i == len(s) {
			res = append(res, strings.Join(state, ""))
			return
		}

		ch := s[i]
		if ch == '{' {
			j := i + 1
			for ; j < len(s); j++ {
				if s[j] == '}' {
					break
				}
			}
			letters := strings.Split(s[i+1:j], ",")

			for _, letter := range letters {
				state = append(state, letter)
				dfs(state, j+1)
				state = state[:len(state)-1]
			}
		} else {
			state = append(state, string(ch))
			dfs(state, i+1)
			state = state[:len(state)-1]
		}
	}
	dfs([]string{}, 0)

	sort.Strings(res)
	return res
}
