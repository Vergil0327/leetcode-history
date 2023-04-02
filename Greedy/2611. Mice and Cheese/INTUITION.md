# Intuition
since we must choose **k** reward1, we can sort rewards by `reward1[i] - reward2[i]` in **decreasing** order and see `reward1[i] - reward2[i]` as the contribution to score.

choose first k largest contribution of reward1, then choose rest of reward from reward2

# Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$
