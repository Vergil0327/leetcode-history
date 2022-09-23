
// example
func unionFind() {
        parent := make([]int, n)
	for i := 0; i < len(parent); i++ {
		parent[i] = i
	}
	rank := make([]int, n)
	for i := 0; i < len(rank); i++ {
		rank[i] = 1
	}

	var find = func(n int) int {
		p := parent[n]

		// path compression
		for p != parent[p] {
			parent[p] = parent[parent[p]]
			p = parent[p]
		}

		return p
	}

	// return false if we can't union n1, n2
	var union = func(n1, n2 int) bool {
		p1, p2 := find(n1), find(n2)
		if p1 == p2 /* already connected */ {
			return false
		}

		if rank[p1] > rank[p2] {
			parent[p2] = p1
			rank[p1] += rank[p2]
		} else {
			parent[p1] = p2
			rank[p2] += rank[p1]
		}

		return true
	}
}
