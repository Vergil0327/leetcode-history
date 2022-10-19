package main

type TrieNode struct {
	next  map[rune]*TrieNode
	isEnd bool
}

func suggestedProducts(products []string, searchWord string) [][]string {
	root := &TrieNode{next: make(map[rune]*TrieNode)}

	// construct Trie
	for _, word := range products {
		curr := root
		for _, ch := range word {
			if _, ok := curr.next[ch]; !ok {
				curr.next[ch] = &TrieNode{next: make(map[rune]*TrieNode)}
			}
			curr = curr.next[ch]
		}
		curr.isEnd = true
	}

	res := [][]string{}
	curr := root
	prefix := ""
	for i, ch := range searchWord {
		// edge case; we can't search any of recommendations
		if _, ok := curr.next[ch]; !ok {
			for j := i; j < len(searchWord); j++ {
				res = append(res, []string{})
			}
			return res
		}

		prefix += string(ch)
		curr = curr.next[ch]

		state := []string{} // recommendations
		dfs(&state, "", curr)

		// append prefix to left
		for i := range state {
			state[i] = prefix + state[i]
		}
		res = append(res, state)
	}

	return res
}

// traverse TrieNode by DFS
// use state to store traversal results
// return recommendations
func dfs(state *[]string, str string, root *TrieNode) {
	if len(*state) == 3 {
		return
	}

	if root.isEnd {
		*state = append(*state, str)
	}

	for i := 0; i < 26; i++ {
		ch := rune('a' + i)
		if _, ok := root.next[ch]; !ok {
			continue
		}

		str += string(ch)
		dfs(state, str, root.next[ch])
		str = str[:len(str)-1] // backtracking
	}
}
