# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
first, I examine these three property 
- **reflexivity**
each character equals itself
a: [a]
b: [b]

- **symmetry**
if a == b, then they can equals each other.
since we need lexicographically smallest one, both `a` and `b` belongs to `[a,b]` group
a: [a, b]
b: [b, a] = [a, b]

- **transitivity**
a: [a, b, c]
b: [b, a]
if a == c, then b == a == c. this means once `a == b`, no matter one of them equals any other character, they are all in the same group

    a: [a,b,c]
    b: [b,a] = [b, [a,b,c]] = b union a = [a,b,c]

it seems like a disjoint set problem, thus, we can use union-find to help us union them into each group.

and we **Always** union lexicographically larger one to lexicographically smaller one

once we have all these groups, we just find character by character in `baseStr` from our union-find, and it'll always find the lexicographically smallest character back to us.

# Approach

1. union `s1` and `s2` character by character
2. find character by character in `baseStr` in our union-find

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(26)$$
