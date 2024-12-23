[1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)

`Medium`

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

```
Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
``` 

Constraints:

- The number of nodes in the tree is in the range [1, 2^10].
- 1 <= Node.val <= 100
- 1 <= distance <= 10

Accepted
52K
Submissions
80.7K
Acceptance Rate
64.5%

<details>
<summary>Hint 1</summary>

Start DFS from each leaf node. stop the DFS when the number of steps done > distance.

</details>
<details>
<summary>Hint 2</summary>

If you reach another leaf node within distance steps, add 1 to the answer.

</details>
<details>
<summary>Hint 3</summary>

Note that all pairs will be counted twice so divide the answer by 2.

</details>