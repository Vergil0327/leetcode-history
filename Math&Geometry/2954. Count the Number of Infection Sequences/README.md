[2954. Count the Number of Infection Sequences](https://leetcode.com/problems/count-the-number-of-infection-sequences/)

`Hard`

You are given an integer n and a 0-indexed integer array sick which is sorted in increasing order.

There are n children standing in a queue with positions 0 to n - 1 assigned to them. The array sick contains the positions of the children who are infected with an infectious disease. An infected child at position i can spread the disease to either of its immediate neighboring children at positions i - 1 and i + 1 if they exist and are currently not infected. At most one child who was previously not infected can get infected with the disease in one second.

It can be shown that after a finite number of seconds, all the children in the queue will get infected with the disease. An infection sequence is the sequential order of positions in which all of the non-infected children get infected with the disease. Return the total number of possible infection sequences.

Since the answer may be large, return it modulo 10^9 + 7.

Note that an infection sequence does not contain positions of children who were already infected with the disease in the beginning.

```
Example 1:
Input: n = 5, sick = [0,4]
Output: 4
Explanation: Children at positions 1, 2, and 3 are not infected in the beginning. There are 4 possible infection sequences:
- The children at positions 1 and 3 can get infected since their positions are adjacent to the infected children 0 and 4. The child at position 1 gets infected first.
Now, the child at position 2 is adjacent to the child at position 1 who is infected and the child at position 3 is adjacent to the child at position 4 who is infected, hence either of them can get infected. The child at position 2 gets infected.
Finally, the child at position 3 gets infected because it is adjacent to children at positions 2 and 4 who are infected. The infection sequence is [1,2,3].
- The children at positions 1 and 3 can get infected because their positions are adjacent to the infected children 0 and 4. The child at position 1 gets infected first.
Now, the child at position 2 is adjacent to the child at position 1 who is infected and the child at position 3 is adjacent to the child at position 4 who is infected, hence either of them can get infected. The child at position 3 gets infected.
Finally, the child at position 2 gets infected because it is adjacent to children at positions 1 and 3 who are infected. The infection sequence is [1,3,2].
- The infection sequence is [3,1,2]. The order of infection of disease in the children can be seen as: [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4].
- The infection sequence is [3,2,1]. The order of infection of disease in the children can be seen as: [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4] => [0,1,2,3,4].

Example 2:
Input: n = 4, sick = [1]
Output: 3
Explanation: Children at positions 0, 2, and 3 are not infected in the beginning. There are 3 possible infection sequences:
- The infection sequence is [0,2,3]. The order of infection of disease in the children can be seen as: [0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3].
- The infection sequence is [2,0,3]. The order of infection of disease in the children can be seen as: [0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3].
- The infection sequence is [2,3,0]. The order of infection of disease in the children can be seen as: [0,1,2,3] => [0,1,2,3] => [0,1,2,3] => [0,1,2,3].
``` 

Constraints:

- 2 <= n <= 10^5
- 1 <= sick.length <= n - 1
- 0 <= sick[i] <= n - 1
- sick is sorted in increasing order.

Accepted
1.8K
Submissions
5.1K
Acceptance Rate
34.8%

<details>
<summary>Hint 1</summary>

Consider infected children as 0 and non-infected as 1, then divide the array into segments with the same value.

</details>
<details>
<summary>Hint 2</summary>

For each segment of non-infected children whose indices are [i, j] and indices (i - 1) and (j + 1), if they exist, are already infected. Then if i == 0 or j == n - 1, each second there is only one kid that can be infected (which is at the other endpoint).

</details>
<details>
<summary>Hint 3</summary>

If i > 0 and j < n - 1, we have two choices per second since the children at the two endpoints can both be the infect candidates. So there are 2j - i + 1 orders to infect all children in the segment.

</details>
<details>
<summary>Hint 4</summary>

Each second we can select a segment and select one endpoint from it.

</details>
<details>
<summary>Hint 5</summary>

The answer is: S! / (len[1]! * len[2]! * ... * len[m]!) * 2k where len[1], len[2], ..., len[m] are the lengths of each segment of non-infected children that have an infected child at both endpoints, S is the total length of all segments of non-infected children, and k = (len[1] - 1) + (len[2] - 1) + ... + (len[m] - 1).

</details>