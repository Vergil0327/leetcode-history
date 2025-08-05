# What is Mo's Algorithm?

Mo's Algorithm is an efficient technique for solving range query problems on a static array, particularly when queries involve computing some property (e.g., sum, count, or frequency) over a range of indices [L, R]. It optimizes query processing by sorting queries in a specific order to minimize the cost of updating the data structure as you move between query ranges. The algorithm is especially useful for problems where:

The array is static (no updates to the array itself).
Queries are offline (all queries are known in advance).
The problem involves computing results over multiple subarrays.

Mo's Algorithm divides the array into blocks of size approximately sqrt(n), where n is the array length, and sorts queries based on their left and right boundaries to process them efficiently. This reduces the time complexity by ensuring that the pointers (L and R) move minimally between consecutive queries.
The typical time complexity of Mo's Algorithm for an array of length n and q queries is O(n * sqrt(n) + q * sqrt(n)), assuming constant-time operations for adding or removing elements in the data structure.

# Intuition

This problem is well-suited for Mo's Algorithm because:

1. Static Array: The array nums is not modified, so all queries operate on the same data.
2. Range Queries: Each query asks for information (frequency of elements) over a specific range [li, ri].
3. Offline Queries: All queries are provided upfront, allowing us to sort them to optimize processing.
4. Frequent Range Adjustments: For each query, you need to compute the frequency of elements in a subarray. Mo's Algorithm minimizes the cost of adjusting the range by maintaining a "window" of indices and updating it efficiently.

Without Mo's Algorithm, a naive approach would process each query independently by scanning the subarray nums[li...ri] and computing frequencies, leading to a time complexity of O(q * n) in the worst case, where q is the number of queries and n is the array length. This is inefficient for large n and q (e.g., n, q ≤ 10^5).
Mo's Algorithm reduces the complexity by:

- Sorting queries to process them in an order that minimizes the movement of the left (L) and right (R) pointers.
- Maintaining a frequency map for the current window and updating it incrementally as the window expands or contracts.



To solve the problem using Mo's Algorithm, follow these steps:

1. Sort Queries:

- Divide the array into blocks of size sqrt(n).
- Sort queries based on:
    - The block index of the left boundary (li // sqrt(n)).
    - Within the same block, sort by the right boundary (ri) in **ascending** order.
    - This ensures that the left pointer moves minimally, and the right pointer moves in a mostly increasing order.




2. Maintain a Frequency Map:

Use a data structure (e.g., a hash map) to track the frequency of elements in the current window [L, R].
Additionally, maintain a frequency-of-frequency map to quickly determine which elements meet the thresholdi requirement and to find the element with the highest frequency.

3. Process Queries:

- Initialize the window [L, R] for the first query.
- For each query [li, ri, thresholdi]:
    - Adjust the window by moving L and R to li and ri, respectively:
        - Add elements to the frequency map when expanding the window (R++ or L--).
        - Remove elements from the frequency map when shrinking the window (R-- or L++).


    - After adjusting the window, check the frequency map to find the smallest element with a frequency at least thresholdi and the highest frequency among such elements.
    - If no such element exists, return -1.