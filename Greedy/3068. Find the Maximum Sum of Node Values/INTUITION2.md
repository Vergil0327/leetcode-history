# Overview

We aim to maximize the sum of values of all nodes in an undirected tree by performing a specific operation.

The operation allows us to replace the values of any two adjacent nodes with their XOR values, with a given integer k.

# Key Observations:

1. Alice can perform an operation on any edge [u, v] by XOR-ing the values of nodes u and v with a positive integer k.
2. Alice wants to maximize the sum of the values of the tree nodes. This means she aims to maximize the total value represented by the sum of individual node values after performing the specified operations.
3. Alice can perform the operation any number of times (including zero) on the tree. This implies she can selectively choose edges and perform the XOR operation to maximize the sum of node values.

> Note: The XOR (exclusive OR) operator compares corresponding bits of two operands and returns 1 if the bits are different and 0 if they are the same. For instance, in binary 1010XOR1100=01101010 XOR 1100 = 01101010XOR1100=0110 indicating that the second and third bits differ while the first and fourth bits are the same.
Bitwise XOR operation is commutative and associative. That means aXORbXORb=aa XOR b XOR b = aaXORbXORb=a, and aXORb=bXORaa XOR b = b XOR aaXORb=bXORa. Hence, the order of applying XOR operations doesn't matter.

> XORing a number with itself (aXORaa XOR aaXORa) results in 000. Therefore, performing the XOR operation twice on the same number yields the original number.

# Approach 1: Top-Down Dynamic Programming - Memoization

## Intuition
Let's assume we want to replace the values of any two arbitrary nodes U and V with their XOR values, where U and V are not adjacent. Since, the tree is connected, undirected, and acyclic, there always exists a path between U and V. Let's assume the length of this path is L and P={P1,P2,P3...PL−1}denotes the set of nodes on this path, following the order in which they appear on the path from U to V. Below is a diagram for better understanding:

U - P1 - P2 - P3 - ... - P{L-1} - V => total size = L

Now, let's operate on every edge from U to V. Since, there are exactly L edges between both the nodes, we will be performing L operations in total.

The value of each node after these L operations will change as shown below:

```
U - P1 - P2 - P3 - ... - P{L-1} - V
nums[U] = nums[U] XOR K

nums[P1] = nums[P1] XOR K XOR K
nums[P2] = nums[P2] XOR K XOR K
nums[P3] = nums[P3] XOR K XOR K
nums[P4] = nums[P4] XOR K XOR K
...
nums[P{L-1}] = nums[P{L-1}] XOR K XOR K

nums[V] = nums[V] XOR K
```

Since the XOR operation obeys the properties of commutativity and identity, **A  XOR  B  XOR  B = A** for any two integers A and B. Therefore, the values of all nodes in the set P will remain unchanged. However, for the nodes U and V, their value will be replaced with the XOR value with k.

So, for any two non-adjacent nodes U and V in the tree we can replace their values with the XOR values as if they were connected by an edge. Let's call this operation as "effective operation" for simplicity.

After performing a sequence of effective operations on some pairs of nodes, exactly m nodes in the tree have their value replaced with the XOR value (where m <= n and n denotes the number of nodes in the tree). It can be observed that the value of m will always be even because "effective operation" is performed on a pair of nodes.

Now, the brute force approach is based on recursion. During recursion, it's crucial to incorporate both: the node's value with XOR operation (XORing with k) and without XOR operation while traversing the tree. We try to maximize the total sum of the values, where the operation is performed on an even number of nodes.

Let's adapt our recursive solution based on these insights:

- The base case occurs when we have traversed through all the nodes of the tree. If the number of nodes on which we have performed the operation is even, we return 0. Otherwise, we return INT_MIN (minimum integer value).

- We also need to include the parity of the number of elements on which the operation has been performed as a parameter in the recursive solution. If the number of operated elements is even, it is a valid assignment.

> Parity of a number refers to whether it contains an odd or even number of 1-bits.

- The two choices that we have here for every node are to perform an operation on it or not. The recursive calls for each case can be explained as:

  - If we perform the operation on the node at the position index, then the value of this node would be modified to nums[index] XOR k. Since we are operating on a node, the parity of the total number of elements on which the XOR operation has been performed will be flipped. Therefore, even parity flips to odd, and vice versa. To obtain the answer for this case, we will store the sum of nums[index] XOR k and the subsequent recursive function call for the next node at index+1 and the flipped parity (denoted by isEven XOR 1).

  - If we do not perform the operation on the node at the position index, then the value of this node would remain the same. The parity of the total number of elements on which the operation is performed will remain the same. To obtain the answer for this case, we will store the sum of nums[index] and the subsequent recursive function call for the next node at index+1 and the given parity.

- Since we want to maximize the sum of all nodes, we will return the maximum value of both the cases discussed above.

The recursive approach will result in Time Limit Exceeded (TLE) issues due to the exponential nature of possibilities.

To tackle this issue, we'll use dynamic programming (DP) with a two-dimensional table.

The DP table caches the results of subproblems, with rows representing different indices of the nodes given by index and columns representing the parity of the number of operated nodes denoted by isEven(0 indicates odd, 1 indicates even parity). Each cell stores an integer denoting the maximum possible sum of all the nodes up to index and where the parity of the number of operated nodes is isEven.

By caching the calculated states in the dp table, we can avoid recalculating the result for the same combination of index and parity. When encountering a state that has already been computed and stored in the dp table, instead of recursively exploring further, we can directly retrieve the cached result, significantly reducing the time complexity of the algorithm.

Algorithm

Main Function: maximumValueSum(nums, k, edges)

1. Initialize a 2D memoization array memo with all values set to -1.
2. Call the helper function maxSumOfNodes with the initial parameters:
   - index = 0
   - isEven = 1 (start with an odd number of elements)
   - nums = the input array
   - k = the given XOR value
   - memo = the initialized memoization array
3. Return the result from the maxSumOfNodes function.

Recursive Function: maxSumOfNodes(index, isEven, nums, k, memo)
1. If the index is equal to the size of the nums array, return:
   - If isEven is 1, return 0 (no operation performed on an odd number of elements).
   - Else, return INT_MIN.
2. If the result for the current index and isEven is already memoized, return the memoized value.
3. Calculate the maximum sum of nodes in two cases:
   - noXorDone: No XOR operation is performed on the current element.
The sum is the current element value nums[index] plus the maximum sum of the remaining elements.
xorDone: The XOR operation is performed on the current element.
The sum is the current element value nums[index] ^ k plus the maximum sum of the remaining elements with isEven flipped.
4. Memoize the maximum of noXorDone and xorDone, and return the result.


## Complexity Analysis

Let n be the number of nodes in the tree.

Time complexity: O(n)

The time complexity of the maxSumOfNodes function can be analyzed by considering the number of unique subproblems that need to be solved. There are at most n⋅2 unique subproblems, indexed by index and isEven values, because the number of possible values for index is n and isEven is 2 (parity).

Here, each subproblem is computed only once (due to memoization). So, the time complexity is bounded by the number of unique subproblems.

Therefore, the time complexity can be stated as O(n).

Space complexity: O(n)

The space complexity of the algorithm is primarily determined by two factors: the auxiliary space used for memoization and the recursion stack space. The memoization table, denoted as memo, consumes O(n) space due to its size being proportional to the length of the input node list.

Additionally, the recursion stack space can grow up to O(n) in the worst case, constrained by the length of the input node list, as each recursive call may add a frame to the stack.

Therefore, the overall space complexity is the sum of these two components, resulting in O(n)+O(n), which simplifies to O(n).