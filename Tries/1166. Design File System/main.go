package main

import "strings"

type TrieNode struct {
	next map[string]*TrieNode
	val  int
}

type FileSystem struct {
	root *TrieNode
}

func NewFileSystem() FileSystem {
	return FileSystem{root: &TrieNode{next: make(map[string]*TrieNode), val: -1}}
}

func (fs *FileSystem) CreatePath(path string, value int) bool {
	if path == "" || !strings.Contains(path, "/") {
		return false
	}

	curr := fs.root
	paths := strings.Split(path, "/")[1:] // skip first ""
	for i, p := range paths {             // /a/b/c => ["", a, b, c]
		if _, ok := curr.next[p]; !ok {
			if i == len(paths)-1 {
				curr.next[p] = &TrieNode{next: make(map[string]*TrieNode), val: -1}
			} else {
				return false // parent didn't exist
			}
		}
		curr = curr.next[p]
	}

	if curr.val != -1 {
		return false // path we want to create has already existed
	}

	curr.val = value
	return true
}

func (fs *FileSystem) get(path string) int {
	paths := strings.Split(path, "/")[1:]

	tri := fs.root
	for _, p := range paths {
		if _, ok := tri.next[p]; !ok {
			return -1
		}
		tri = tri.next[p]
	}

	return tri.val
}
