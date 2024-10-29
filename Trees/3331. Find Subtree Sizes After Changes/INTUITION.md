# Intuition

1. 先求出final tree:
    - 每個節點沿著parent一路往上, 找到最近的字符相同parent後, 更新該節點的parent
2. 用post-order dfs求出每個節點的subtree size