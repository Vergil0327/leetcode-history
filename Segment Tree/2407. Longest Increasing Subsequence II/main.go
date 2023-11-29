// https://leetcode.com/problems/longest-increasing-subsequence-ii/

package main

import "math"

// https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2560085/Python-Explanation-with-pictures-Segment-Tree
func lengthOfLIS(nums []int, k int) int {
	n := 0
	for _, num := range nums {
		if num > n {
			n = num
		}
	}
	ans := 1
	seg := NewSegmentTree(n)

	/*
		[7,4,5,1,8,12,4,7], k=5
		the longest length: 4 ([4,5,8,12])
		segment tree:0 1 2 3 4 5 6 7 8 9    12
		{n:12, tree:[0 1 1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0]}
		{n:12, tree:[0 1 1 1 1 0 0 1 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0]}
		{n:12, tree:[0 2 2 1 2 0 0 1 2 1 0 0 0 0 0 1 2 0 1 0 0 0 0 0]}
		{n:12, tree:[0 2 2 1 2 0 1 1 2 1 0 0 1 0 0 1 2 0 1 0 0 0 0 0]}
		{n:12, tree:[0 3 3 1 3 0 1 1 2 3 0 0 1 0 0 1 2 0 1 3 0 0 0 0]}
		{n:12, tree:[0 4 4 1 3 4 1 1 2 3 0 4 1 0 0 1 2 0 1 3 0 0 0 4]}
		{n:12, tree:[0 4 4 2 3 4 1 2 2 3 0 4 1 0 0 2 2 0 1 3 0 0 0 4]}
		{n:12, tree:[0 4 4 2 3 4 1 2 2 3 0 4 1 0 0 2 2 0 3 3 0 0 0 4]}
	*/
	for _, num := range nums {
		// check for the element in the range of [nums[i] - k, nums[i] - 1] with the maximum value
		num -= 1 // offset 1 to 0-index
		l, r := int(math.Max(0, float64(num-k))), num
		premax := seg.Query(l, r)
		ans = int(math.Max(float64(ans), float64(premax+1)))
		seg.Update(num, premax+1)
	}

	return ans
}

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

// Time Limit Exceed
func lengthOfLIS_TLE(nums []int, k int) int {
	LIS := make([]int, len(nums))
	for i := range LIS {
		LIS[i] = 1
	}

	for i := len(nums) - 1; i >= 0; i-- {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] < nums[j] && nums[j]-nums[i] <= k {
				LIS[i] = max(LIS[i], 1+LIS[j])
			}
		}
	}

	max := 0
	for _, v := range LIS {
		if v > max {
			max = v
		}
	}

	return max
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
