// https://leetcode.com/problems/word-ladder/

package main

/*
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
*/

// think undirected graph
func ladderLength(beginWord string, endWord string, wordList []string) int {
	graph := buildGraph(append(wordList, beginWord))

	if _, ok := graph[endWord]; !ok {
		return 0
	}

	// bfs
	count := 0
	visited := map[string]bool{}
	// predecessor := map[string]string{}
	queue := []string{beginWord}

	// BFS: T:O(E+V), v stands for vertices & E for total number of edges in graph
	// T:O(n^2*m), n^2 from iteration through all the edges, m for comparison between words
	for len(queue) > 0 {
		count += 1
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
