### Accepted

not the best efficient solution but I think is easy to understand

#### Intuition

1. mainly use `preorder` to find root node
2. `postorder` can help us to find right node's index since root node's previous node is always right node
3. then we can split `preorder` into left portion & right portion
4. lastly, we can just like [leetcode 105](../105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/) and [leetcode 106](../106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal/) to construct the whole binary tree back


### Optimized

we can further optimize solution by using `hashmap` to store value-index mapping of `postorder`

#### Intuition

use two pointer `l` & `r` to represent our valid `preorder` range

1. mainly use `preorder` to find root node
2. use `l` & `r` to define our left subtree and right subtree
   1. root node will be `preorder[l]`
   2. left node will be `preorder[l+1]`
   3. then, we can use `postorder` to find left subtree's size
   4. once we know the left subtree's size, we can know the right subtree's size
3. recursively construct our binary tree