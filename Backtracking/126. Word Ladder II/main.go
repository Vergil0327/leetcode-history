package main

// two visited hashmap idea -> ref: https://www.youtube.com/watch?v=bGN7c34qzCg
func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	foundEnd := false

	neighbors := map[string][]string{} // pattern: [word1, word2, ...]
	for _, word := range wordList {
		if word == endWord {
			foundEnd = true
		}

		// construct neighbors by pattern
		// AAA -> *AA, A*A, AA*
		// BAA -> *AA, B*A, BA*
		// => *AA: [AAA, BAA] we can get transform sequence by same pattern
		for i := 0; i < len(word); i++ {
			pattern := word[:i] + "*" + word[i+1:]
			neighbors[pattern] = append(neighbors[pattern], word)
		}
	}

	if !foundEnd {
		return nil
	}

	trace := map[string][]string{} // trace node's parent (previous node). we can backtrace from endWord later
	visited := map[string]bool{}
	trace[beginWord] = make([]string, 0)
	visited[beginWord] = true

	queue := []string{beginWord}
	foundEnd = false
	for len(queue) > 0 && !foundEnd {
		currVisited := map[string]bool{}

		for _, word := range queue {
			queue = queue[1:]
			for i := 0; i < len(word); i++ {
				pattern := word[:i] + "*" + word[i+1:]
				for _, candidate := range neighbors[pattern] {
					// if we reach visited node again, it won't be shortest path
					if visited[candidate] {
						continue
					}

					// word can be duplicate because node can be used in different path
					trace[candidate] = append(trace[candidate], word)

					// we don't want to push candidate into queue more than once
					// or we'll try to find the same node's candidate more than once. (wrong duplicate)
					if currVisited[candidate] {
						continue
					}
					currVisited[candidate] = true
					queue = append(queue, candidate)
				}
			}
		}

		// A -> B -> C -> end
		// A -> E -> C -> end
		// we must update visited after finish current level of traversal, or we'll miss other path that also cross C node
		// update visited to avoid push duplicate into the queue
		for word := range currVisited {
			visited[word] = true
			if word == endWord {
				foundEnd = true
			}
		}
	}

	res := [][]string{}

	// find path from endWord along trace path
	var backtracking func(state []string, word string)
	backtracking = func(state []string, word string) {
		if len(trace[word]) == 0 {
			// because we start from endWord, append at beginning
			state = append([]string{word}, state...)
			res = append(res, state)
		} else {
			for _, prev := range trace[word] {
				backtracking(append([]string{word}, state...), prev)
			}
		}

	}

	if !foundEnd {
		return nil
	}

	backtracking([]string{}, endWord)

	return res
}

// ref: https://leetcode.com/problems/word-ladder-ii/discuss/40493/The-fastest-golang-solution-using-bfs-(275ms-beats-100.00-of-golang-submissions)
func findLaddersUseMapAsQueue(beginWord string, endWord string, wordList []string) [][]string {
	foundEnd := false
	trace := map[string][]string{}     // trace path from beginWord to endWord
	neighbors := map[string][]string{} // pattern: [word1, word2, ...]
	for _, word := range wordList {
		trace[word] = make([]string, 0)
		if word == endWord {
			foundEnd = true
		}

		for i := 0; i < len(word); i++ {
			pattern := word[:i] + "*" + word[i+1:]
			neighbors[pattern] = append(neighbors[pattern], word)
		}
	}

	if !foundEnd {
		return nil
	}

	visited := map[string]bool{}
	queue := map[string]struct{}{}
	queue[beginWord] = struct{}{}
	trace[beginWord] = make([]string, 0)
	visited[beginWord] = true

	_, ok := queue[endWord]
	for len(queue) > 0 && !ok {
		currVisited := map[string]bool{}
		next := map[string]struct{}{}
		for word := range queue {
			for i := 0; i < len(word); i++ {
				pattern := word[:i] + "*" + word[i+1:]
				for _, candidate := range neighbors[pattern] {
					if visited[candidate] {
						continue
					}

					currVisited[candidate] = true

					trace[candidate] = append(trace[candidate], word)
					next[candidate] = struct{}{}
				}
			}
		}

		// A -> B -> C -> end
		//      E -> C -> end
		// we must update visited after finish current level of queue, or we'll miss other path that also cross C node
		// update visited to avoid push duplicate into the queue
		for word := range currVisited {
			visited[word] = true
		}

		queue = next
		_, ok = queue[endWord]
	}

	res := [][]string{}

	// find path from endWord along trace path
	var backtracking func(state []string, word string)
	backtracking = func(state []string, word string) {
		if len(trace[word]) == 0 {
			// because we start from endWord, append at beginning
			state = append([]string{word}, state...)
			res = append(res, state)
		} else {
			for _, prev := range trace[word] {
				backtracking(append([]string{word}, state...), prev)
			}
		}

	}

	// edge case: if queue is empty, it means we don't have transformation sequence to reach endWord
	// begin:"hot", end:"dog"
	// ["hot","dog"]
	if len(queue) != 0 {
		backtracking([]string{}, endWord)
	}

	return res
}
