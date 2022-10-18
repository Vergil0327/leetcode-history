package main

func areSentencesSimilarTwo(words1, words2 []string, pairs [][2]string) bool {
	if len(words1) != len(words2) {
		return false
	}

	parent := map[string]string{}

	var find = func(word string) string {
		if _, ok := parent[word]; !ok {
			parent[word] = word
			return word
		}

		p := parent[word]
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	// construct Union-Find Disjoint Set
	for _, pair := range pairs {
		left, right := pair[0], pair[1]
		pl, pr := find(left), find(right)

		if pl != pr {
			parent[pl] = pr // union
		}
	}

	for i, word := range words1 {
		if find(word) != find(words2[i]) {
			return false
		}
	}

	return true
}
