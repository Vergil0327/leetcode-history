// https://leetcode.com/problems/word-search-ii/
package main

import (
	"fmt"
	"strings"
)

type TrieNode struct {
	children  map[rune]*TrieNode
	endOfWord bool
}

type Trie struct {
	root *TrieNode
}

func (t *Trie) Insert(word string) {
	curr := t.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			curr.children[c] = &TrieNode{children: make(map[rune]*TrieNode)}
		}
		curr = curr.children[c]
	}
	curr.endOfWord = true
}

func (t *Trie) Search(word string) bool {
	curr := t.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}

	return curr.endOfWord
}
func (t *Trie) StartsWith(prefix string) bool {
	curr := t.root
	for _, c := range prefix {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}

	return true
}

// https://leetcode.com/problems/word-search-ii/discuss/59780/Java-15ms-Easiest-Solution-(100.00)
func findWordsOptimized(board [][]byte, words []string) []string {
	trie := Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
	for _, word := range words {
		trie.Insert(word)
	}

	res := []string{}

	var backtracking func(state string, i, j int, node *TrieNode)
	backtracking = func(state string, i, j int, node *TrieNode) {
		c := rune(board[i][j])
		curr := node

		if _, ok := node.children[c]; !ok {
			return
		}

		if c == '#' {
			return
		}

		state += string(c)
		node = node.children[c]
		if node.endOfWord { // found one
			res = append(res, state)
			node.endOfWord = false // ! prevent duplicate
		}

		// If I am at a leaf, there is no further exploration and I can truncate the leaf
		if len(node.children) == 0 {
			delete(curr.children, c)
			return
		}

		board[i][j] = '#'
		if i < len(board)-1 {
			backtracking(state, i+1, j, node)
		}
		if i > 0 {
			backtracking(state, i-1, j, node)
		}
		if j < len(board[0])-1 {
			backtracking(state, i, j+1, node)
		}
		if j > 0 {
			backtracking(state, i, j-1, node)
		}

		// backtracking, restore
		board[i][j] = byte(c)
	}

	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[0]); c++ {
			backtracking("", r, c, trie.root)
		}
	}

	return res
}

// explanation: https://www.youtube.com/watch?v=asbcE9mZz_U
func findWords(board [][]byte, words []string) []string {
	trie := Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
	for _, word := range words {
		trie.Insert(word)
	}

	res := map[string]struct{}{}
	visited := map[string]bool{}
	var backtracking func(state string, i, j int, node *TrieNode)
	backtracking = func(state string, i, j int, node *TrieNode) {
		rowInBounds := i >= 0 && i < len(board)
		colInBounds := j >= 0 && j < len(board[0])
		if !(rowInBounds && colInBounds) {
			return
		}

		if _, ok := node.children[rune(board[i][j])]; !ok {
			return
		}

		key := fmt.Sprintf("%d,%d", i, j)
		if existed, ok := visited[key]; existed && ok {
			return
		}

		visited[key] = true

		c := rune(board[i][j])
		state += string(c)
		node = node.children[c]
		if node.endOfWord {
			res[state] = struct{}{}
		}

		backtracking(state, i+1, j, node)
		backtracking(state, i-1, j, node)
		backtracking(state, i, j+1, node)
		backtracking(state, i, j-1, node)
		visited[key] = false
	}

	for r := 0; r < len(board); r++ {
		for c := 0; c < len(board[0]); c++ {
			backtracking("", r, c, trie.root)
		}
	}

	keys := []string{}
	for k := range res {
		keys = append(keys, k)
	}
	return keys
}

// Timeout
func findWordsTimeout(board [][]byte, words []string) []string {
	trie := Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}

	for _, word := range words {
		trie.Insert(word)
	}

	// res := []string{} // ! will contain duplicates
	res := map[string]struct{}{}

	var backtracking func(state []string, i, j int, visited map[string]bool)
	backtracking = func(state []string, i, j int, visited map[string]bool) {
		if str := strings.Join(state, ""); !trie.StartsWith(str) {
			return
		}

		rowInBounds := i >= 0 && i < len(board)
		colInBounds := j >= 0 && j < len(board[0])
		if !(rowInBounds && colInBounds) {
			return
		}

		key := fmt.Sprintf("%d,%d", i, j)
		if existed, ok := visited[key]; ok && existed {
			return
		}

		visited[key] = true
		state = append(state, string(board[i][j]))

		if str := strings.Join(state, ""); trie.Search(str) {
			// res = append(res, str) // ! will contain duplicates
			res[str] = struct{}{}
		}

		backtracking(state, i+1, j, visited)
		backtracking(state, i-1, j, visited)
		backtracking(state, i, j+1, visited)
		backtracking(state, i, j-1, visited)

		visited[key] = false
		// state = state[:len(state)-1] // redundant
	}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			backtracking([]string{}, i, j, map[string]bool{})
		}
	}

	keys := []string{}
	for k := range res {
		keys = append(keys, k)
	}
	return keys
}

func findWordsTimeout2(board [][]byte, words []string) []string {
	trie := Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}

	for _, word := range words {
		trie.Insert(word)
	}

	res := map[string]struct{}{} // remove duplicates

	var backtracking func(state string, i, j int, visited map[string]bool)
	backtracking = func(state string, i, j int, visited map[string]bool) {
		if !trie.StartsWith(state) {
			return
		}

		rowInBounds := i >= 0 && i < len(board)
		colInBounds := j >= 0 && j < len(board[0])
		if !(rowInBounds && colInBounds) {
			return
		}

		key := fmt.Sprintf("%d,%d", i, j)
		if existed, ok := visited[key]; ok && existed {
			return
		}

		visited[key] = true
		state += string(board[i][j])

		if trie.Search(state) {
			res[state] = struct{}{}
		}

		backtracking(state, i+1, j, visited)
		backtracking(state, i-1, j, visited)
		backtracking(state, i, j+1, visited)
		backtracking(state, i, j-1, visited)

		visited[key] = false
	}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			backtracking("", i, j, map[string]bool{})
		}
	}

	keys := []string{}
	for k := range res {
		keys = append(keys, k)
	}
	return keys
}
