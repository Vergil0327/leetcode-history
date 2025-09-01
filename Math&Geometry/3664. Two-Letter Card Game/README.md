[3664. Two-Letter Card Game](https://leetcode.com/problems/two-letter-card-game/)

`Medium`

You are given a deck of cards represented by a string array cards, and each card displays two lowercase letters.

You are also given a letter x. You play a game with the following rules:

Start with 0 points.
On each turn, you must find two compatible cards from the deck that both contain the letter x in any position.
Remove the pair of cards and earn 1 point.
The game ends when you can no longer find a pair of compatible cards.
Return the maximum number of points you can gain with optimal play.

Two cards are compatible if the strings differ in exactly 1 position.

```
Example 1:
Input: cards = ["aa","ab","ba","ac"], x = "a"
Output: 2
Explanation:

On the first turn, select and remove cards "ab" and "ac", which are compatible because they differ at only index 1.
On the second turn, select and remove cards "aa" and "ba", which are compatible because they differ at only index 0.
Because there are no more compatible pairs, the total score is 2.

Example 2:
Input: cards = ["aa","ab","ba"], x = "a"
Output: 1
Explanation:

On the first turn, select and remove cards "aa" and "ba".
Because there are no more compatible pairs, the total score is 1.

Example 3:
Input: cards = ["aa","ab","ba","ac"], x = "b"
Output: 0
Explanation:

The only cards that contain the character 'b' are "ab" and "ba". However, they differ in both indices, so they are not compatible. Thus, the output is 0.
```

Constraints:

- 2 <= cards.length <= 10^5
- cards[i].length == 2
- Each cards[i] is composed of only lowercase English letters between 'a' and 'j'.
- x is a lowercase English letter between 'a' and 'j'.

Accepted
5,131/61.5K
Acceptance Rate
8.3%

<details>
<summary>Hint 1</summary>

Compute both, cnt1[c], cnt2[c] as the counts of cards with x in both positions, only the first position (other letter c), and only the second position.

</details>
<details>
<summary>Hint 2</summary>

Let solve(cnt, have) be the maximum pairs you can form from one‐sided counts cnt plus have two‐sided cards by sorting cnt, computing the total, and applying the same logic as in the solution.

</details>
<details>
<summary>Hint 3</summary>

Return the maximum over i = 0..both of solve(cnt1, i) + solve(cnt2, both - i).

</details>