Template of Binary Search Tree

```python
def BST(root, target):
    if target == root.val:
        # do something
    if target < root.val:
        BST(root.left, target)
    if target > root.val:
        BST(root.right, target)
```

1. if what we want to delete is in the left subtree, we update our left subtree

```python
root.left = deleteBST(root.left, target)
```

2. if what we want to delete is in the right subtree, we update our right subtree

```python
root.right = deleteBST(root.right, target)
```

3. if we found the target node:
    since we need to maintain BST's feature, let's discuss all the possible cases:
    1. target node has `NO` child nodes. no left and no right child node
       ```python
       if not root.left and not root.right: return None
       ```
    2. target node only has `ONE` child node
        ```python
        if not root.left: return root.right
        if not root.right: return root.left
        ```
    3. target node has left & right child node simultaneously
        since we need to maintain BST's feature (left < root < right),
        we need to replace current root node with one of `larget node in left subtree` or `smallest node in right subtree`
        ```python
        minNode = root.right
        while minNode.left:
            minNode = minNode.left
        
        # delete minNode
        root.right = deleteBST(root.right, minNode)

        # replace root node with minNode
        # remember to update reference to left and right child node
        minNode.left = root.left
        minNode.right = root.right
        root = minNode
        ```

thus, our delete logic becomes

```python
if root.val == target:
    # these two condition already cover case of `not root.left and not root.right`
    if not root.left: return root.right
    if not root.right: return root.left

    minNode = root.right
    while minNode.left:
        minNode = minNode.left

    root.right = deleteBST(root.right, minNode)

    minNode.left = root.left
    minNode.right = root.right
    root = minNode
    return root
```