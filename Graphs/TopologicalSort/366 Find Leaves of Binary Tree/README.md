366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this:
  - Collect all the leaf nodes.
  - Remove all the leaf nodes.
  - Repeat until the tree is empty.

Example1:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2
 

2. Now removing the leaf [2] would result in this tree:

          1
 

3. Now removing the leaf [1] would result in the empty tree:

          []

Example 2:

Input: root = [1]
Output: [[1]]

Constraints:

- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100

```go
type TreeNode struct {
	Val         int
	Left, Right *TreeNode
}
func findLeaves(root *TreeNode) [][]int {
  if root == nil {
    return nil
  }

  inDegrees := map[*TreeNode]int{}
  queue := []*TreeNode{root}
  for len(queue) > 0 {
    for _, node := range queue {
      queue = queue[1:]

      if _, ok := inDegrees[node]; !ok {
        inDegrees[node] = 0
      }

      if node.Left != nil {
        inDegrees[node] += 1
        queue = append(queue, node.Left)
      }
      if node.Right != nil {
        inDegrees[node] += 1
        queue = append(queue, node.Right)
      }
    }
  }

  res := make([][]int, len(inDegrees))
  queue = make([]*TreeNode, 0)
  for node, deg := range inDegrees {
    if deg == 0 {
        queue = append(queue, node)
    }
  }

  i := 0
  for len(queue) > 0 {
    for _, node := range queue {
      queue = queue[1:]

      if res[i] == nil {
        res[i] = make([]int, 0)
      }
      res[i] = append(res[i], node.Val)

      if node.Left != nil {
        inDegrees[node.Left] -= 1
        if inDegrees[node.Left] == 0 {
          queue = append(queue, node.Left)
        }
      }
      if node.Right != nil {
        inDegrees[node.Right] -= 1
        if inDegrees[node.Right] == 0 {
          queue = append(queue, node.Right)
        }
      }
    }
    i+=1
  }

  return res
}
```