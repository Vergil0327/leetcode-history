// https://leetcode.com/problems/word-ladder/

package main

/*
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
*/

// explanation: https://www.youtube.com/watch?v=h9iTnkgv05E
// T:O(nm^2), m for word length, n for wordList length
// m < n, m <= 10 & n <= 5000
// therefore, T:O(nm^2) is greater than T:O(mn^2)
func ladderLengthOptimized(beginWord string, endWord string, wordList []string) int {
	includeEndWord := false
	for _, word := range wordList {
		if word == endWord {
			includeEndWord = true
		}
	}
	if !includeEndWord {
		return 0
	}

	graph := map[string][]string{}
	for _, word := range append(wordList, beginWord) {
		for j := range word {
			pattern := word[:j] + "*" + word[j+1:]
			graph[pattern] = append(graph[pattern], word)
		}
	}

	visited := map[string]bool{}
	queue := []string{beginWord}
	count := 1 // already has beginWord
	for len(queue) > 0 {
		for _, word := range queue {
			queue = queue[1:]

			if word == endWord {
				return count
			}

			if _, ok := visited[word]; ok {
				continue
			}

			visited[word] = true

			for j := range word {
				pattern := word[:j] + "*" + word[j+1:]
				for _, neighbor := range graph[pattern] {
					if _, ok := visited[neighbor]; !ok {
						queue = append(queue, neighbor)
					}
				}
			}
		}

		count += 1
	}

	return 0
}

// think undirected graph
func ladderLength(beginWord string, endWord string, wordList []string) int {
	graph := buildGraph(append(wordList, beginWord))

	if _, ok := graph[endWord]; !ok {
		return 0
	}

	// bfs
	count := 1 // already one word exists
	visited := map[string]bool{}
	// predecessor := map[string]string{}
	queue := []string{beginWord}

	// BFS: T:O(E+V), v stands for vertices & E for total number of edges in graph
	// T:O(n^2*m), n^2 from iteration through all the edges, m for comparison between words
	for len(queue) > 0 {
		for _, word := range queue {
			// T:O(1) for deque item
			queue = queue[1:]

			if existed, ok := visited[word]; existed && ok {
				continue
			}

			visited[word] = true

			// T:O(m)
			if word == endWord {
				return count
			}

			// T:O(E)
			for _, neighbor := range graph[word] {
				if existed, ok := visited[neighbor]; !existed || !ok {
					// predecessor[neighbor] = word
					queue = append(queue, neighbor)
				}
			}
		}
		count += 1
	}

	return 0
}

// T:O(n) M:O(1)
func canTransform(word1, word2 string) bool {
	wordLen := len(word1)
	i, j := 0, 0
	count := 0
	for i < wordLen && j < wordLen {
		if word1[i] != word2[j] {
			count += 1
		}
		i, j = i+1, j+1
	}

	return count == 1
}

func buildGraph(wordList []string) map[string][]string {
	// T:O(n)
	graph := map[string][]string{}
	for _, word := range wordList {
		graph[word] = make([]string, 0)
	}

	// T:O(n^2)
	for key := range graph {
		for _, word := range wordList {
			if key == word {
				continue
			}

			if canTransform(key, word) {
				graph[key] = append(graph[key], word)
			}
		}
	}

	return graph
}
