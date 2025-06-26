# Intuition

let's define dfs return the longest zig-zag path from each leaf node

1. we tag each node with direction first by using pre-order traversal.
    ```py
    LEFT, RIGHT = 0, 1
    def dfs(root, direct):
        if not root: return 0

        left = dfs(root.left, LEFT)
        right = dfs(root.right, RIGHT)
    ```
2. and we can calculate path length at post-order DFS position
   1. if currect node is left child node(`direct==LEFT`), it can only append to zig-zag path whose direction ends at right
      -  path length = `1+right` and current zig-zag direction ends with `direct`
   2. if current node is right child node(`direct==RIGHT`), it can only apppend to zig-zag path whose direction ends at left
      -  path length = `1+left` and current zig-zag direction ends with `direct`

    ```py
    def dfs(root, direct):
        if not root: return 0
        left = dfs(root.left, LEFT)
        right = dfs(root.right, RIGHT)
        
        if direct == LEFT:
            return 1+right
        elif direct == RIGHT:
            return 1+left
        else:
            return max(left+1, right+1)
    ```

3. and we find longest path from `max(left, right)`
   ```py
    left = dfs(root.left, LEFT)
    right = dfs(root.right, RIGHT)
    self.res = max(self.res, left, right)
   ``` 