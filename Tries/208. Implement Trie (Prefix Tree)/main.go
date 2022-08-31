// https://www.youtube.com/watch?v=oobqoCJlHA0
package main

type TrieNode struct {
	children  map[rune]*TrieNode
	endOfWord bool
}

// Explanation: https://www.youtube.com/watch?v=oobqoCJlHA0
type Trie struct {
	root *TrieNode
}

func Constructor() Trie {
	return Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
}

func (this *Trie) Insert(word string) {
	curr := this.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			curr.children[c] = &TrieNode{children: make(map[rune]*TrieNode)}
		}
		curr = curr.children[c]
	}
	curr.endOfWord = true
}

func (this *Trie) Search(word string) bool {
	curr := this.root
	for _, c := range word {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}
	return curr.endOfWord
}

func (this *Trie) StartsWith(prefix string) bool {
	curr := this.root
	for _, c := range prefix {
		if _, ok := curr.children[c]; !ok {
			return false
		}
		curr = curr.children[c]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
