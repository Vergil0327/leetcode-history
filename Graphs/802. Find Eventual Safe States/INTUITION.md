# Intuition

```
DFS(node) -> 如果該次DFS能走到最後, 則該路線為True
          -> 條件是每一條路線都得為True
          -> 如果有Cycle那直接返回False, 代表該node至少有一條走不到termination node
```
遍歷過程中若每個DFS都為True, 則將該node加入到safe nodes裡

最後排序並返回全部safe nodes即可