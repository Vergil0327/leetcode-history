# Greedy

## Intuition

alice與bob交互拿石頭，雙方對石頭的得分不同並且拿走後對方不可再拿
如此一來，獲勝的最佳策略便是`優先拿兩方石頭分數加總最高的石頭`

因為拿走的同時，自己得分高的同時對方能拿的分數也減少得最多，能拉開雙方最多的差距

因此這題可以套用Greedy Algorithm

## Approach

1. 加總兩方的石頭，並以此由大到小排序便是取石頭的優先順序
2. alice & bob兩方交替拿，並各自加總分數
3. 最後再比較兩者分數即可

## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$
