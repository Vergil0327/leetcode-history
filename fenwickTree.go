// https://tobin.cc/blog/fenwick/

package leetcode

type Fenwick struct {
	tree []int
}

// NewFenwick: Build Fenwick tree to hold n values.
func NewFenwick(n int) *Fenwick {
	fen := &Fenwick{
		tree: make([]int, n+1),
	}
	return fen
}

// Sum all values upto and including index.
func (fen *Fenwick) Sum(index int) int {
	sum := 0
	index++ // fenwick tree is 1-based
	for index > 0 {
		sum += fen.tree[index]
		index -= lsb(index)
	}
	return sum
}

// lsb: Least Significant Bit
func lsb(x int) int {
	return x & -x
}

// Update using addition index by value.
func (fen *Fenwick) Update(index, delta int) {
	index++ // fenwick tree is 1-based
	for index <= fen.Size() {
		fen.tree[index] += delta
		index += lsb(index)
	}
}

// Size: Number of values stored by tree.
func (fen *Fenwick) Size() int {
	return len(fen.tree)
}
