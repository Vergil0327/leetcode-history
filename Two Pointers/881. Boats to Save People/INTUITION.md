# Intuition
since there are only 2 people on the boat at most, we must pair heaviest person with light-weight one.

it's kind of greedy approach:
1. handle those weight same as limit or can't pair with even the lightest weight person, they must take boat alone.
2. then we pair the heaviest person with lightest weight person

it may end up with l == r, don't forget to check this condition,
we need 1 more boat for this person

# Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(1)$$
