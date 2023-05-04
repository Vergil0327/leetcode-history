# Intuition

simulate the voting process

- `cur`: current round of voting
- `nxt`: next rount of voting

- for each round, one by one in order and greedily ban another party's member if current senate's not banned.
  - store how many ban exists in `ban` hashmap
- once current round finish, all the survivors continue voting at next round until all the remain members belongs to one party
  - use hashmap `exists` to check how many kinds of senate still exist in voting.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
