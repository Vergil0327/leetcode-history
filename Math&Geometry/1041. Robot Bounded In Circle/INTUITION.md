# Intuition

如果最後會留在圈內:
1. 沿著軸方向來回走 => 方向變換兩次
2. 沿著矩形方向繞圈走 => 方向變換四次

所以我們先循環四次找出四個方向走到得最遠距離
然後再走四次循環看最後位置, 如果超出第一次循環走的位置, 代表會越走越遠

# Optimized

如果根據指示`instructions`走完:

1. 最後回到原點
2. 或是最後方向不是一開始的[0,1]

那最後路徑勢必會是個封閉圖形, 詳見[@lee215](https://leetcode.com/problems/robot-bounded-in-circle/solutions/290856/java-c-python-let-chopper-help-explain)