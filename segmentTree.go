// https://www.geeksforgeeks.org/iterative-segment-tree-range-minimum-query/
// The iterative version of the segment tree:
// for an index i, left child = 2 * i and right child = 2 * i + 1 in the tree.
// The parent for an index i in the segment tree array can be found by parent = i / 2
// Segment Tree by 花花: https://www.youtube.com/watch?v=rYBtViWXYeI
// Segment Tree by OTTFF: https://www.youtube.com/watch?v=s7vZDDpeR7w
// 影片圖解: https://www.youtube.com/watch?v=Oq2E2yGadnU
type SegmentTree struct {
	n    int
	tree []int
}

func NewSegmentTree(n int) SegmentTree {
	return SegmentTree{n: n, tree: make([]int, 2*n)}
}

// Basically the left and right indices
// will move towards right and left respectively
// and with every each next higher level and
// compute the minimum at each height change
// the index to leaf node first
// T:O(log(n))
func (t *SegmentTree) Query(l, r int) int {
	// leaf node
	l += t.n
	r += t.n

	ans := 0
	for l < r {
		// if left index is odd (it's right child node, it's not covered from higher level)
		if l&1 == 1 {
			ans = int(math.Max(float64(ans), float64(t.tree[l])))
			l += 1
		}

		// if right index is odd (if it's even, it's covered by next higher level, i.e. it's parent node)
		if r&1 == 1 {
			r -= 1
			ans = int(math.Max(float64(ans), float64(t.tree[r])))
		}

		// move to the next higher level
		l >>= 1
		r >>= 1
	}

	return ans
}

func (t *SegmentTree) Update(i, val int) {
	i += t.n        // change the index to leaf node first
	t.tree[i] = val // update the value at the leaf node at the exact index
	for i > 1 {
		// move up one level at a time in the tree
		i >>= 1

		// update the values in the nodes in the next higher level
		t.tree[i] = int(math.Max(float64(t.tree[i*2]), float64(t.tree[i*2+1])))
	}
}