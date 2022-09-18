// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
package main

type TrieNode struct {
	c       map[byte]*TrieNode
	visited int
}

// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/discuss/2590081/C%2B%2B-Java-Python3-Easy-Trie-Explained-with-diagram
// T:O(total characters)
func sumPrefixScores(words []string) []int {
	// calculate score of all the prefixes
	trie := &TrieNode{}
	for _, word := range words {
		curr := trie
		for i := 0; i < len(word); i++ {
			// lazy init
			if curr.c == nil {
				curr.c = make(map[byte]*TrieNode)
			}
			if curr.c[word[i]] == nil {
				curr.c[word[i]] = &TrieNode{}
			}

			curr.c[word[i]].visited += 1
			curr = curr.c[word[i]]
		}
	}

	res := []int{}
	for _, word := range words {
		t := trie
		score := 0
		for i := 0; i < len(word); i++ {
			score += t.c[word[i]].visited
			t = t.c[word[i]]
		}

		res = append(res, score)
	}

	return res
}

// T:O(n^3)
func sumPrefixScoresBruteForce(words []string) []int {
	res := make([]int, len(words))
	for i := range words {
		for _, w := range words {
			j := 0
			for j < len(w) && j < len(words[i]) {
				if w[j] == words[i][j] {
					res[i] += 1
				} else {
					break
				}
				j += 1
			}
		}
	}

	return res
}
