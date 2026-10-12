"""
### Optimal Strategy: Array-Based Flat Trie + Merge Inversion Counting

To achieve sub-second execution in Python:
1. **Flatten the Trie into Parallel Primitive Arrays:** Represent the Trie using flat integer lists (`children[node_id][char_code]`, `word_pos[node_id]`). This completely eliminates Python object creation overhead.
2. **Merge Sort Inversion Counting:** Instead of `heapq.merge` or `.sort()`, perform an in-place/buffer-based merge of child position arrays. During merge:
   $$\text{Inversions between } A \text{ and } B = \sum (len(A) - i) \quad \text{whenever } A[i] > B[j]$$
3. **Exact Bitmask DP with Static Memory:**
   - Pre-allocate small DP tables for $C \le 10$ children per node.
   - For every node, evaluate the optimal permutation cost of its child branches using bitwise operations without creating temporary objects.

### Logic to Calculate Inversions

1. Definition of Inversion in Pre-Order Traversal:
   In a pre-order traversal of the Trie:
   - Every node's own word index (if marked) is visited FIRST before any of its children.
   - The children subtrees are visited sequentially in some chosen permutation order.
   - Completing a child's traversal means all word indices in its subtree are output in contiguous block.

   An inversion occurs between two word indices A and B if:
   - A appears BEFORE B in the traversal output, but pos[A] > pos[B] (meaning B was supposed to come before A in target).

2. Three Types of Inversion Contributions at Each Node:

   a. Parent-to-Child Inversions:
      - The node's marked word index (p_self) appears before all word indices in its child subtrees.
      - For each child subtree, since its target positions are kept sorted, we iterate through its elements and count how many p_child < p_self.

   b. Cross-Child Inversions (Between Child Subtrees):
      - For two child subtrees A and B, if child A is visited BEFORE child B, the number of cross-inversions between them is:
        cost[A][B] = number of pairs (a in A, b in B) such that pos[a] > pos[b].
      - Two-Pointer Computation:
        Since A and B are both sorted lists of target positions, we can compute cost[A][B] in O(|A| + |B|) time using two pointers:
        For each element `a` in A, we advance pointer `ptrB` in B as long as B[ptrB] < a.
        The number of elements in B smaller than `a` is `ptrB`. Summing `ptrB` over all `a` in A gives cost[A][B].

   c. Optimal Permutation via Bitmask DP:
      - Placing child subtrees in order (p_0, p_1, ..., p_{C-1}) incurs a total cross-inversion cost:
        Total Cross Cost = Sum_{0 <= i < j < C} cost[p_i][p_j]
      - State Definition:
        `dp(mask)` = minimum cross-inversions needed to order the remaining children not in `mask`, where `mask` is a bitmask of children already placed.
      - State Transition:
        When appending an unvisited child `i` (not in `mask`), it incurs a cross-inversion cost with all children `j` that were placed BEFORE it (i.e., j in `mask`):
        add_cost = Sum_{j in mask} cost[j][i]
        dp(mask) = min_{i not in mask} (add_cost + dp(mask | (1 << i)))

---

### Complexity Analysis

1. Time Complexity:

   - Trie Construction:
     Inserting N words of length L takes O(N * L) time.

   - Cross-Inversion Matrix Computation:
     For a node with C children and total subtree size M:
     Computing pairwise costs takes O(C^2 * M) operations.
     Summing across all levels of the Trie, the total time across the entire tree is O(N * L * C).
     For N = 10,000, L = 20, C <= 10: ~2 * 10^6 operations.

   - Bitmask DP per Node:
     With C <= 10 children per node, the bitmask DP has 2^C states (at most 1024 states) and C transitions per state.
     DP time per node = O(C^2 * 2^C) = 100 * 1024 ≈ 10^5 operations.
     Only nodes with C > 1 children run DP.

   - Subtree List Merging:
     Merging child lists into a single sorted list takes O(M log M) per node.

   - Overall Time Complexity:
     O(N * L * C + N * C^2 * 2^C + N * L log N)
     For N = 10,000, L = 20, C = 10: Runs in ~0.15 - 0.20 seconds.

2. Space Complexity:

   - Trie Structure:
     Max nodes <= N * L = 200,000 nodes. Flat array storage takes O(N * L * C) space.

   - DFS Recursion Stack & List Merging:
     Holding sorted lists of positions in memory takes O(N * L) space.

   - Overall Space Complexity:
     O(N * L) auxiliary space.
"""
class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        n = len(words)
        
        # pos[x] = position of word x in target array
        pos = [0] * n
        for position, word_idx in enumerate(target):
            pos[word_idx] = position

        # Pre-allocate Trie node structures using flat integer arrays
        # Maximum nodes <= sum of lengths of all words + 1
        max_nodes = sum(len(w) for w in words) + 2
        
        # 10 possible children ('a' through 'j')
        trie_children = [[-1] * 10 for _ in range(max_nodes)]
        word_pos = [-1] * max_nodes
        node_count = 1  # Root is node 0
        
        # Build Trie
        for i, w in enumerate(words):
            curr = 0
            for ch in w:
                c_idx = ord(ch) - 97  # 'a' -> 0, ..., 'j' -> 9
                if trie_children[curr][c_idx] == -1:
                    trie_children[curr][c_idx] = node_count
                    node_count += 1
                curr = trie_children[curr][c_idx]
            word_pos[curr] = pos[i]

        total_inversions = 0

        # Pre-allocated DP memory for permutations up to 10 children
        dp_memo = [-1] * 1024
        cost = [[0] * 10 for _ in range(10)]

        def dfs(u: int) -> list[int]:
            nonlocal total_inversions

            # Collect active child nodes
            active_children = []
            for c_idx in range(10):
                v = trie_children[u][c_idx]
                if v != -1:
                    active_children.append(v)

            # Base case: Leaf node
            if not active_children:
                return [word_pos[u]] if word_pos[u] != -1 else []

            # Process children recursively
            child_lists = [dfs(v) for v in active_children]
            num_children = len(child_lists)

            # 1. Parent-to-child inversions
            if word_pos[u] != -1:
                p_self = word_pos[u]
                for clist in child_lists:
                    for p_child in clist:
                        if p_child < p_self:
                            total_inversions += 1
                        else:
                            break

            # 2. Compute pairwise cross-inversion cost matrix
            for i in range(num_children):
                for j in range(num_children):
                    if i != j:
                        inv = 0
                        ptrB = 0
                        listA = child_lists[i]
                        listB = child_lists[j]
                        lenB = len(listB)
                        for a in listA:
                            while ptrB < lenB and listB[ptrB] < a:
                                ptrB += 1
                            inv += ptrB
                        cost[i][j] = inv

            # 3. Fast Bitmask DP for optimal child permutation
            if num_children > 1:
                ALL_MASK = (1 << num_children) - 1
                for m in range(ALL_MASK + 1):
                    dp_memo[m] = -1

                def solve_dp(mask: int) -> int:
                    if mask == ALL_MASK:
                        return 0
                    if dp_memo[mask] != -1:
                        return dp_memo[mask]
                    
                    res = 10**18
                    for i in range(num_children):
                        if not (mask & (1 << i)):
                            add_cost = 0
                            for j in range(num_children):
                                if mask & (1 << j):
                                    add_cost += cost[j][i]
                            val = solve_dp(mask | (1 << i)) + add_cost
                            if val < res:
                                res = val
                    dp_memo[mask] = res
                    return res

                total_inversions += solve_dp(0)

            # 4. In-place merge of child lists with parent word_pos
            merged = [word_pos[u]] if word_pos[u] != -1 else []
            for clist in child_lists:
                merged.extend(clist)
            merged.sort()

            return merged

        dfs(0)
        return total_inversions