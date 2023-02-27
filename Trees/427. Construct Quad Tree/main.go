package leetcode427

/**
 * Definition for a QuadTree node.
 */
type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func construct(grid [][]int) *Node {
	n := len(grid)

	var build func(r0, r1, c0, c1 int) *Node
	build = func(r0, r1, c0, c1 int) *Node {
		if r1 == r0 && c1 == c0 {
			var val bool
			if grid[r0][c0] == 1 {
				val = true
			}
			return &Node{Val: val, IsLeaf: true}
		}

		midR := r0 + (r1-r0)/2
		midC := c0 + (c1-c0)/2
		topLeft := build(r0, midR, c0, midC)
		bottomLeft := build(midR+1, r1, c0, midC)
		topRight := build(r0, midR, midC+1, c1)
		bottomRight := build(midR+1, r1, midC+1, c1)
		if topLeft.IsLeaf && bottomLeft.IsLeaf && topRight.IsLeaf && bottomRight.IsLeaf && topLeft.Val == bottomLeft.Val && bottomLeft.Val == topRight.Val && topRight.Val == bottomRight.Val {
			return &Node{Val: bottomRight.Val, IsLeaf: true}
		}

		return &Node{Val: false, IsLeaf: false, TopLeft: topLeft, TopRight: topRight, BottomLeft: bottomLeft, BottomRight: bottomRight}
	}
	return build(0, n-1, 0, n-1)
}
