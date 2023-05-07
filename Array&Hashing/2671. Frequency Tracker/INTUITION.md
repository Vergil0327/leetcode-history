# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
first think what kind of data strctures do we need ?

- we need to record frequency of every added `number`:
    - use hashmap `counter`
- we still need to be able to check if frequency exists or not
    - use another hashmap `freq` to store every frequency existing in `counter`, then we can use O(1) time to check.

then we just update these 2 hashmap in each API.

- add:
    - update `counter`: counter[num] += 1
    - udpate `freq`: decrement old freq and increment new freq.
- deleteOne:
    - update `counter`: counter[num] -= 1
    - update `freq`: decrement old freq and increment new freq.
- hasFrequency:
    - no need to update

# Complexity
- Time complexity:
$$O(1)$$

- Space complexity:
$$O(n)$$
