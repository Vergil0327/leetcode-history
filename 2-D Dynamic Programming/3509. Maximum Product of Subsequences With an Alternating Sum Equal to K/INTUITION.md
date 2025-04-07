# Intuition

要找一個合法subset, 可以用top-down dp去找出最大值合法product

定義`def dfs(i, sign, total, prod, picked)`返回the maximum product of the numbers in valid subsequence

但由於product可能會很大, 這邊可以用個小技巧是透過`limit+1`來加個上限
這樣一來complexity就能縮到`O(n*2*sum(nums)*(limit+1)*2)`