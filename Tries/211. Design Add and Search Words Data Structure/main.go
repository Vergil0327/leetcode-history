// https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/
package main

type TrieNode struct {
	children  map[rune]*TrieNode
	endOfWord bool
}

type WordDictionary struct {
	root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{root: &TrieNode{children: make(map[rune]*TrieNode)}}
}

func (this *WordDictionary) AddWord(word string) {
	curr := this.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			curr.children[c] = &TrieNode{children: make(map[rune]*TrieNode)}
		}
		curr = curr.children[c]
	}
	curr.endOfWord = true
}

// explanation: https://www.youtube.com/watch?v=BTf05gs_8iU
func (this *WordDictionary) Search(word string) bool {
	const ANY = '.'
	var dfs func(j int, root *TrieNode) bool
	dfs = func(j int, root *TrieNode) bool {
		curr := root

		for i := j; i < len(word); i++ {
			c := rune(word[i])

			if c == ANY {
				for _, childNode := range curr.children {
					if dfs(i+1, childNode) {
						return true
					}
				}
				return false
			} else {
				if _, ok := curr.children[c]; !ok {
					return false
				}
				curr = curr.children[c]
			}
		}

		return curr.endOfWord
	}

	return dfs(0, this.root)
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
