// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/alien-dictionary/
// https://www.lintcode.com/problem/892/
package main

import "strings"

/*
Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
]
Output: ""
*/

/**
 * @param words: a list of words
 * @return: a string which is correct order
 */
func AlienOrderBFS(words []string) string {
	graph := buildGraph(words)
	inDegrees := map[string]int{}
	for k, edges := range graph {
		if _, ok := inDegrees[k]; !ok {
			inDegrees[k] = 0
		}

		for _, edge := range edges {
			inDegrees[edge] += 1
		}
	}

	queue := []string{}
	for letter, deg := range inDegrees {
		if deg == 0 {
			queue = append(queue, letter)
		}
	}

	order := []string{}
	for len(queue) > 0 {
		for _, word := range queue {
			queue = queue[1:]

			order = append(order, word)

			for _, nei := range graph[word] {
				inDegrees[nei] -= 1
				if inDegrees[nei] == 0 {
					queue = append(queue, nei)
				}
			}
		}
	}

	if len(order) == len(graph) {
		return strings.Join(order, "")
	}

	return ""
}

// https://www.youtube.com/watch?v=6kTZYvNNyps
func AlienOrderDFS(words []string) string {
	graph := buildGraph(words)

	cycle := map[string]struct{}{}

	// topological order from dfs would be reversed
	order := []string{}

	var dfs func(src string) bool
	dfs = func(src string) bool {
		if _, ok := cycle[src]; ok {
			return true
		}

		// existed: has cycle
		cycle[src] = struct{}{}

		for _, nei := range graph[src] {
			if dfs(nei) {
				return true
			}
		}

		// if cycle doesn't exist, append to order
		order = append(order, src)
		delete(cycle, src)

		return false
	}

	for c := range graph {
		if dfs(c) {
			return ""
		}
	}

	for i, j := 0, len(order)-1; i < j; i, j = i+1, j-1 {
		order[i], order[j] = order[j], order[i]
	}
	return strings.Join(order, "")
}

func buildGraph(words []string) map[string][]string {
	g := map[string][]string{}

	N := len(words)
	for i := 0; i < N-1; i++ {
		word1, word2 := words[i], words[i+1]

		k := 0
		for k < len(word1) && k < len(word2) {
			if _, ok := g[string(word1[k])]; !ok {
				g[string(word1[k])] = make([]string, 0)
			}
			if _, ok := g[string(word2[k])]; !ok {
				g[string(word2[k])] = make([]string, 0)
			}

			if word1[k] != word2[k] {
				g[string(word1[k])] = append(g[string(word1[k])], string(word2[k]))
				break
			}
			k += 1
		}
	}

	return g
}
