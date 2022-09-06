// https://appliedgo.net/balancedtree/

package main

import (
	"fmt"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// max is math.Max for int.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Node gets a new field, height, to store the height of the subtree at this node.
type Node struct {
	Value  string
	Data   string
	Left   *Node
	Right  *Node
	height int
}

// Height returns the height value. Wait, what’s the point? Well, the zero value of *Node is nil. If a child node is nil, there is no heightfield available; however, it is possible to call a method of a nil struct value! As a Go proverb says, “Make the zero value useful”.
func (n *Node) Height() int {
	if n == nil {
		return 0
	}
	return n.height
}

// Bal returns the balance of a node’s subtrees: 0 for a balanced node, +n if the right subtree is n nodes taller than the left, -n if the left subtree is n nodes taller than the right.
func (n *Node) Bal() int {
	return n.Right.Height() - n.Left.Height()
}

func (n *Node) Insert(value, data string) *Node {
	// The node does not exist yet. Create a new one, fill in the data, and return the new node.
	if n == nil {
		return &Node{
			Value:  value,
			Data:   data,
			height: 1,
		}
	}
	// The node already exists: update the data and all is good. Actually, this is Upsert semantics. (“Upsert” is a coinage made from “Update or Insert”.) Alternatively, Insert could return an error here, and an extra Update method would be required for updating existing data.
	if n.Value == value {
		n.Data = data
		return n
	}

	if value < n.Value {
		// The new value is smaller than the current node’s value, hence insert it into the left subtree.
		n.Left = n.Left.Insert(value, data)
	} else {
		// Larger values are inserted into the right subtree.
		n.Right = n.Right.Insert(value, data)
	}
	// At this point, one of the subtrees might have grown by one. The current node’s height thus needs to be re-calculated.

	n.height = max(n.Left.Height(), n.Right.Height()) + 1
	// Also, the subtree at node n might be out of balance.
	return n.rebalance()
}

func (n *Node) rotateLeft() *Node {
	fmt.Println("rotateLeft " + n.Value)
	// Save n's right child in r.
	r := n.Right
	// Move r's right subtree to the left of n.
	n.Right = r.Left
	// Then, make n the left child of r.
	r.Left = n
	// Finally, re-calculate the heights of n and r.
	n.height = max(n.Left.Height(), n.Right.Height()) + 1
	r.height = max(r.Left.Height(), r.Right.Height()) + 1
	// Return the new top node of this part of the tree.
	return r
}

// rotateRight is the mirrored version of rotateLeft.
func (n *Node) rotateRight() *Node {
	fmt.Println("rotateRight " + n.Value)
	l := n.Left
	n.Left = l.Right
	l.Right = n
	n.height = max(n.Left.Height(), n.Right.Height()) + 1
	l.height = max(l.Left.Height(), l.Right.Height()) + 1
	return l
}

// rotateRightLeft first rotates the right child of c to the right, then c to the left.
func (n *Node) rotateRightLeft() *Node {
	n.Right = n.Right.rotateRight()
	n = n.rotateLeft()
	n.height = max(n.Left.Height(), n.Right.Height()) + 1
	return n
}

// rotateLeftRight first rotates the left child of c to the left, then c to the right.
func (n *Node) rotateLeftRight() *Node {
	n.Left = n.Left.rotateLeft()
	n = n.rotateRight()
	n.height = max(n.Left.Height(), n.Right.Height()) + 1
	return n
}

// rebalance brings the (sub-)tree with root node c back into a balanced state.
func (n *Node) rebalance() *Node {
	fmt.Println("rebalance " + n.Value)
	n.Dump(0, "")
	switch {
	// Left subtree is too high, and left child has a left child.
	case n.Bal() < -1 && n.Left.Bal() == -1:
		return n.rotateRight()
		// Right subtree is too high, and right child has a right child.
	case n.Bal() > 1 && n.Right.Bal() == 1:
		return n.rotateLeft()
		// Left subtree is too high, and left child has a right child.
	case n.Bal() < -1 && n.Left.Bal() == 1:
		return n.rotateLeftRight()
		// Right subtree is too high, and right child has a left child.
	case n.Bal() > 1 && n.Right.Bal() == -1:
		return n.rotateRightLeft()
	}
	return n
}

// Find stays the same as in the previous article.
func (n *Node) Find(s string) (string, bool) {

	if n == nil {
		return "", false
	}

	switch {
	case s == n.Value:
		return n.Data, true
	case s < n.Value:
		return n.Left.Find(s)
	default:
		return n.Right.Find(s)
	}
}

// Dump dumps the structure of the subtree starting at node n, including node search values and balance factors. Parameter i sets the line indent. lr is a prefix denoting the left or the right child, respectively.
func (n *Node) Dump(i int, lr string) {
	if n == nil {
		return
	}
	indent := ""
	if i > 0 {
		indent = strings.Repeat(" “, (i-1)*4) + “+” + strings.Repeat(”-", 3)
		indent = strings.Repeat(" ", (i-1)*4) + "+" + lr + "--"
	}
	fmt.Printf("%s%s[%d,%d]\n", indent, n.Value, n.Bal(), n.Height())
	n.Left.Dump(i+1, "L")
	n.Right.Dump(i+1, "R")
}

/*
Tree
Changes to the Tree type:

Insert now takes care of rebalancing the root node if necessary.
A new method, Dump, exist for invoking Node.Dump.
Delete is gone.
*/
type Tree struct {
	Root *Node
}

func (t *Tree) Insert(value, data string) {
	t.Root = t.Root.Insert(value, data)
	// If the root node gets out of balance,
	if t.Root.Bal() < -1 || t.Root.Bal() > 1 {
		t.rebalance()
	}
}

// Node's rebalance method is invoked from the parent node of the node that needs rebalancing. However, the root node of a tree has no parent node. Therefore, Tree’s rebalance method creates a fake parent node for rebalancing the root node.
func (t *Tree) rebalance() {
	if t == nil || t.Root == nil {
		// Nothing to balance here.
		return
	}
	t.Root = t.Root.rebalance()
}

// Find receives a value s and returns true if t contains s.
func (t *Tree) Find(s string) (string, bool) {
	if t.Root == nil {
		return "", false
	}
	return t.Root.Find(s)
}

// Traverse traverses the tree t depth-first and executes f on each node.
func (t *Tree) Traverse(n *Node, f func(*Node)) {
	if n == nil {
		return
	}
	t.Traverse(n.Left, f)
	f(n)
	t.Traverse(n.Right, f)
}

// PrettyPrint prints the tree at a 90° angle, with the root to the left and the leaves to the right. This function is very simplistic and works only well for single-character values. Otherwise we would need to know the maximum length of all values of a given tree level in advance, in order to format the tree properly.
func (t *Tree) PrettyPrint() {

	printNode := func(n *Node, depth int) {
		fmt.Printf("%s%s\n", strings.Repeat("  ", depth), n.Value)
	}
	// walk has to be declared explicitly. Otherwise the recursive walk() calls inside walk would not compile.
	var walk func(*Node, int)
	walk = func(n *Node, depth int) {
		if n == nil {
			return
		}
		walk(n.Right, depth+1)
		printNode(n, depth)
		walk(n.Left, depth+1)
	}

	walk(t.Root, 0)
}

// Dump dumps the tree structure.
func (t *Tree) Dump() {
	t.Root.Dump(0, "")
}
