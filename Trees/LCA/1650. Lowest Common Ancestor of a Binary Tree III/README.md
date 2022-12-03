[1650. Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)

`Medium`

*SUBSCRIBE TO UNLOCK*

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

```
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
```

Constraints:

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q exist in the tree.

<details>
<summary>Solution</summary>

[Huifeng Guan](https://github.com/wisdompeak/LeetCode/tree/master/Tree/1650.Lowest-Common-Ancestor-of-a-Binary-Tree-III)
</details>

<details>
<summary>Another Solution</summary>

[ref](https://labuladong.github.io/algo/2/21/47/)

```java
class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        // 区别：本题没有根节点
        
        // 找到根节点
        Node *parent = p; // 从p开始找起
        while(parent->parent){
            if(parent == q){
                return parent;
            }
            parent = parent->parent;
        }

        return lca(parent,p,q);
    }
    Node* lca(Node* node,Node *p,Node *q){
        // base case
        if(node == nullptr){
            return nullptr;
        }

        if(node->val == p->val || node->val == q->val){
            return node;
        }
        Node *left = lca(node->left,p,q);
        Node *right = lca(node->right,p,q);
        if(left && right){
            return node;
        }

        return left == nullptr ? right : left;

    }
};

```

```java
class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        // 双链表相交问题
        Node *a = p;
        Node *b = q;

        while(a!=b){
            a = a == nullptr ? q : a->parent;
            b = b == nullptr ? p : b->parent;
        }

        return a;
    }
};
```
</details>