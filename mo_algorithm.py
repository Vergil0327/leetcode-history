"""
# What is Mo's Algorithm?

Mo's Algorithm is an efficient technique for solving range query problems on a static array, particularly when queries involve computing some property (e.g., sum, count, or frequency) over a range of indices [L, R]. It optimizes query processing by sorting queries in a specific order to minimize the cost of updating the data structure as you move between query ranges. The algorithm is especially useful for problems where:

The array is static (no updates to the array itself).
Queries are offline (all queries are known in advance).
The problem involves computing results over multiple subarrays.

Mo's Algorithm divides the array into blocks of size approximately sqrt(n), where n is the array length, and sorts queries based on their left and right boundaries to process them efficiently. This reduces the time complexity by ensuring that the pointers (L and R) move minimally between consecutive queries.
The typical time complexity of Mo's Algorithm for an array of length n and q queries is O(n * sqrt(n) + q * sqrt(n)), assuming constant-time operations for adding or removing elements in the data structure.

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
"""

# ex. 3636. Threshold Majority Queries