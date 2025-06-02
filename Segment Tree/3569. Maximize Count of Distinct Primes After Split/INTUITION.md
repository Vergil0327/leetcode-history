# Intuition

Given an array nums and a list of queries, for each query you:

1. Update nums[idx] = val.
2. Split the array into a prefix and suffix at position k (1 ≤ k < n).
3. Calculate the number of distinct prime values in both parts.
4. Find the split that maximizes the total number of distinct primes and return this number.
5. Repeat for all queries.

### Key Ideas

- Use a prime sieve to quickly check primality.
- Track the first and last occurrences of each prime.
- Use a Lazy Segment Tree to efficiently track the count of distinct primes across segments.
- Only track updates for distinct prime intervals.


- Each prime p is considered as a "segment" [first_index_of_p, last_index_of_p].

- A valid split k includes this prime if the segment crosses the split point.

- So the number of overlapping prime segments at each k is the sum we care about.

- The segment tree efficiently maintains and updates these overlapping counts.