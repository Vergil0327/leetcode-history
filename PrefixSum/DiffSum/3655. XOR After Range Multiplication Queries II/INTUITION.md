# Intuition

> Hint: For k <= B (where B = sqrt(n)): group queries by (k, l mod k); for each group maintain a diff-array of length ceil(n/k) to record multiplier updates, then sweep each bucket to apply them to nums.

XOR 特性, 兩個同數值的數會抵銷
所以重點是要能有效紀錄每個queries[i]最後總共對各個nums[j]乘上多少次`v`, 兩兩相同就相消, 這樣最終只要計算那些還留下來的數就好

快速標記想到difference array, 但由於每個queries[i]都對for i in range(l, r+1, k)跳著更新, 所以很難利用difference array
但因為都是間隔`k`去跳著更新, 所以我們應該是可以把同間隔的視為相同的group


l1 + k, l1 + 2*k, l1 + 3*k, ... => 假設l1 = a1 + m * k
l2 + k, l2 + 2*k, l2 + 3*k, ... => 假設l2 = a2 + m * k
如果a1 == a2, 也就是(l1 % k) == (l2 % k), 那麼他們就會是在相同間隔更新的同個group裡
把這類型的聚在一起, 先後順序定下來, 是不是就能用difference array來快速標記並更新總相乘次數了?

底下是@AlexWice的解法, 其實是一樣概念, difference array變成標記乘數的array

In a (l, r, k, v) query, if k is larger than N, we only do O(N) work multiplying the subsequence manually.

Let's focus on small k. For each position i and jump length k, we can let events[k][i] = v denote that we want to multiply A[i], A[i+k], A[i+2k], ... by v.

Then multiplying a segment is equal to two events: events[k][l] *= v and events[k][r2] *= inverse(v). Here, r2 is the smallest r2 > r that is on the path l, l+k, ... and so has residue modulo k equal to l.