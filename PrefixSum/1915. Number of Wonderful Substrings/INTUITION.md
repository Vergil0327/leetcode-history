# Intuition - Hashing + Prefix Sum

the number of prefix[i] - the number of prefix[j] => at most 1 character has odd frequencies in 26 characters

since we only care parity, record prefix as 26-bit mask and 0 means even, 1 means odd
=> prefix_bit_state = prefix_bit_state ^ (1<<(ord(s[i])-ord("a")))

then we can use **hashmap** to store { prefix_bitmask: the number of substring } and check if there exists valid prefix[j] in **hashmap** such that prefix[i]-prefix[j] contains at most 1 odd frequency character

therefore:

1. 0 odd character:
    - prefix[i]^prefix[j] = 0 => prefix[j] = prefix[i] => res += seen[prefix]
2. 1 odd character at most:
    - iterate `a` to `j` to check if there exists a substr whose `a` to `j` character contains 1 odd frequency
    - if prefix_bit contains `ch` which means all the other characters must even => `res += seen[prefix^(1<<i)]`
    - if there is no `ch` in prefix_bit, it means `prefix[j] = prefix|(1<<i)` => `res += seen[prefix|(1<<i)]`
    - actually, we can combine these two to `res += seen[prefix^(1<<i)]`. there is no different.

it's kind of intuitively think bitmask with 10 EN characters and 0/1, XOR operation with parity

# Complexity

- time complexity

    $$O(10n)$$

- space complexity

    $$O(2^10)$$

