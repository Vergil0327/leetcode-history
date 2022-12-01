[765. Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)

`Hard`

There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

```
Example 1:
Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.
```

Constraints:

- 2n == row.length
- 2 <= n <= 30
- n is even.
- 0 <= row[i] < 2n
- All the elements of row are unique.

<details>
<summary>Hint</summary>

Say there are N two-seat couches. For each couple, draw an edge from the couch of one partner to the couch of the other partner.
</details>

<details>
<summary>solution</summary>

[HuifengGuan](https://github.com/wisdompeak/LeetCode/tree/master/Union_Find/765.Couples-Holding-Hands)

[HuifengGuan - video explanation](https://www.youtube.com/watch?v=hihj4Y7I1jA)
</details>

<details>
<summary>other solution</summary>

这道题的思路比较巧妙。

首先，每个人都有一个 person_id，person_id 相邻的两个人被认为是一对情侣，即 (0, 1), (2, 3) ...

那如果我想给「每对情侣」给一个 couple_id，从 0 到 n - 1，如何分配？

可以把 person_id / 2 作为 couple_id，因为每对情侣的 person_id 相邻，除以二向下取整之后结果相同：

0 / 2 == 1 / 2 == 0，2 / 2 == 3 / 2 == 1 ...
在理想情况下，每对情侣坐在一起，结合 Union Find 算法 将 couple_id 相同的两个节点相连，最终应该有 n 个联通分量。

但实际上并不是每对情侣都坐在正确的位置上，所以会有多对情侣进入了同一个连通分量，导致连通分量的数量变少，n 和连通分量只差就是需要交换的次数，可以自行画图理解。

```java
class Solution {
    public int minSwapsCouples(int[] row) {
        int n = row.length;
        UF uf = new UF(n);
        for (int i = 0; i < n; i += 2) {
            // 将两人的 couple_id 进行连接
            uf.union(row[i] / 2, row[i + 1] / 2);
        }
        // 和连通分量的差即为需要交换的次数
        return n - uf.count();
    }
}

// 并查集算法模板
class UF {
    // 记录连通分量个数
    private int count;
    // 存储若干棵树
    private int[] parent;

    public UF(int n) {
        this.count = n;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    /* 将 p 和 q 连通 */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)
            return;

        parent[rootQ] = rootP;
        count--;
    }

    /* 判断 p 和 q 是否互相连通 */
    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        // 处于同一棵树上的节点，相互连通
        return rootP == rootQ;
    }

    /* 返回节点 x 的根节点 */
    private int find(int x) {
        while (parent[x] != x) {
            // 进行路径压缩
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int count() {
        return count;
    }
}
```
</details>