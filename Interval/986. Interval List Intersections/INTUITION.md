# Sweepline with Two Pointers

## Intuition

since two list are sorted, we use two pointers `i` & `j` to iterate `firstList` & `secondList`

    use two pointers `i`, `j` to compare, always start from smallest startTime. sweepline through all intervals


first, we skip non-overlapping interval:
1. firstList[i][1] < secondList[j][0]
2. secondList[i][1] < firstList[j][0]

then all we have are overlapping interval.

we keep continue to compare firstList[i] with secondList[j]

see illustration:
```
.--------. .------.
    .--------. .------.
```

there are two cases:
- first[i][1] overlap with second[j][0], firstList's tail with secondList's head
- first[i][0] overlap with second[j][1], firstList's head with secondList's tail

these two cases all generate this intersection: `[max(first[i][0], second[j][0]), min(first[i][1], second[j][1])]`

we just append to results and move pointer with small startTime

## Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(1)$$

# More Compact & Concise

我们用 [a1, a2] 和 [b1, b2] 表示在 A 和 B 中的兩個區間，如果這兩個區間有交集，需滿足b2 >= a1 && a2 >= b1，分四種情況

1. 
.--------.
  .--.

2. 
.--------.
  .------------.

3. 
    .---.
.------------.

4. 
    .--------.
.--------.

根據上面四種可發現規律，假設交集的區間為[c1,c2]，那麼:
- c1 = max(a1, b1)
- c2 = min(a2, b2)

因此當滿足`b2 >= a1 && a2 >= b1`時，交集區域為`[max(a1, b1), min(a2, b2)]`

如果我們在考慮沒交集的區域的話
5. 
.----.
        .----.
6. 
        .----.
.----.

會發現5, 6兩種的[c1,c2]會是 `max(a1, b1) > min(a2, b2)`
所以我們也能判斷當`c1 <= c2`時，才會有交集的[c1,c2]區間

兩者比較完後移動endTime較小的那邊
