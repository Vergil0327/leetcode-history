# Greedy

## Intuition

首先我們的目的是刪除最少區間來達到每個區間不相互重疊

首先我們將區間以[startTime, endTime]表示
那我們可以想，如果我們以endTime來由小到大排序然後在遍歷的話:

`當endTime越靠前，往後與其他重疊的機會就越低`

所以每當兩個區間重疊，我們便移除當前這個區間
或者我們將該區間的endTime設為前一個區間的endTime，然後繼續往後遍歷比較

所以每個重疊的區間，便是我們應當移除的區間，紀錄數量即可返回答案

## Further Summary

- sort by starting time
can solve `the minimum number of intervals to cover whole range`

可比較好找出能覆蓋整個範圍的最少區間有哪些

- sort by ending time
can solve `the maximum number of intervals that are non-overlapping

可比較好找出最多不重疊的區間