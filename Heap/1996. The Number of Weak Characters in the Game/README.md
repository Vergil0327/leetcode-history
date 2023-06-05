[1996. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/)

`Medium`

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

```
Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
``` 

Constraints:

- 2 <= properties.length <= 10^5
- properties[i].length == 2
- 1 <= attacki, defensei <= 10^5

Acceptance Rate
43.9%

<details>
<summary>Hint 1</summary>

Sort the array on the basis of the attack values and group characters with the same attack together. How can you use these groups?

</details>

<details>
<summary>Hint 2</summary>

Characters in one group will always have a lesser attack value than the characters of the next group. Hence, we will only need to check if there is a higher defense value present in the next groups.

</details>