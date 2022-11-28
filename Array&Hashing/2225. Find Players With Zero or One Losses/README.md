[2225. Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)

`Medium`

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 
```
Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
```

Constraints:

- 1 <= matches.length <= 10^5
- matches[i].length == 2
- 1 <= winneri, loseri <= 10^5
- winneri != loseri
- All matches[i] are unique.

<details>
<summary>Solution</summary>

[solution](https://leetcode.com/problems/find-players-with-zero-or-one-losses/discuss/1908760/Python-Solution-with-Hashmap)

1. Maintain a hashmap of player and their losses.
2. Traverse this hashmap and check if player has 0 or 1 loss and append to a winners, losers list as necessary.
3. Return the sorted lists.

```python
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers, table = [], [], {}
        for winner, loser in matches:
            # map[key] = map.get(key, 0) + change . This format ensures that KEY NOT FOUND error is always prevented.
            # map.get(key, 0) returns map[key] if key exists and 0 if it does not.
            table[winner] = table.get(winner, 0)  # Winner
            table[loser] = table.get(loser, 0) + 1
        for k, v in table.items(): # Player k with losses v
            if v == 0:
                winners.append(k) # If player k has no loss ie v == 0
            if v == 1:
                losers.append(k) # If player k has one loss ie v == 1
        return [sorted(winners), sorted(losers)] # Problem asked to return sorted arrays.
```
</details>