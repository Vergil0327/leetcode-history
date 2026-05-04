1. The Real Conditions for Valid Subsequences

An element $x = \text{nums}[i]$ can become a fixed point if we delete exactly $i - x$ elements before it. Let's look at what is required to make two original indices $i$ and $j$ ($i < j$) fixed points:

1. $i \ge \text{nums}[i]$ and $j \ge \text{nums}[j]$ (you cannot make negative deletions).
2. The number of deletions before $i$ must be less than or equal to the total deletions up to $j$:
   - $$i - \text{nums}[i] \le j - \text{nums}[j]$$
3. Because the elements maintain their relative order, the new index of $j$ must be strictly greater than the new index of $i$:
   - $$\text{new index}(j) > \text{new index}(i) \implies \text{nums}[j] > \text{nums}[i]$$

Let's test if there is any hidden constraint between the two:

> $$\text{new index}(j) - \text{new index}(i) = \text{nums}[j] - \text{nums}[i]$$

But we know the remaining distance between $j$ and $i$ after deletions is exactly the original distance $(j - i)$ minus the deletions that happened strictly between $i$ and $j$.

> $$\text{deletions between } i \text{ and } j = (j - \text{nums}[j]) - (i - \text{nums}[i])$$

The deletions between $i$ and $j$ cannot exceed the available items between $i$ and $j$. This translates to:

> $$(j - \text{nums}[j]) - (i - \text{nums}[i]) \le j - i - 1 \implies \text{nums}[j] \ge \text{nums}[i] + 1$$

This perfectly aligns with $\text{nums}[i] < \text{nums}[j]$.


2. The Solution Concept: 2D Partial Order

We can treat each valid element as a 2D point:

> $$\text{Point} = (x, y) = (\text{nums}[i], i - \text{nums}[i])$$

For point $A = (v_i, d_i)$ to come before point $B = (v_j, d_j)$, we need:

1. $v_i < v_j$
2. $d_i \le d_j$

This is exactly the Russian Doll Envelopes problem, but with a slight twist: one dimension is strictly increasing while the other is non-decreasing.

To solve it using a standard 1D LIS optimization (using bisect_left/bisect_right):

1. We first filter valid elements where $i \ge \text{nums}[i]$.
2. We sort the candidates by their first parameter $v$ in ascending order.
3. Crucial Tie-breaker: If two elements have the same value $v$, we sort by $d$ in descending order. This prevents us from matching two items with the same $v$, since $v$ must be strictly increasing!

    A Concrete Example
    Let's say after filtering, we have two valid candidates that have the same value $v = 1$, but different original indices. Let's call them A and B:
    - Candidate A: $v = 1, d = 2$ (Original index $i = 3$)
    - Candidate B: $v = 1, d = 4$ (Original index $i = 5$)

    Can we turn both of these into fixed points at the same time? No, because they both have the value 1. You can't have two elements with the value 1 at different indices in the final array.

    Let's see what happens depending on how we sort the ties in $d$:

    - Scenario 1: Sorting ties in $d$ in Ascending order (Incorrect)

    The candidates would be ordered like this:
    - $(1, 2)$
    - $(1, 4)$
    
    Now, we extract the $d$ values to find the Longest Non-Decreasing Subsequence: [2, 4].
    Since $4 \ge 2$, the algorithm thinks [2, 4] is a valid subsequence of length 2.
    It incorrectly picks both A and B. This violates the rule because $v$ didn't increase ($1 \to 1$).

    - Scenario 2: Sorting ties in $d$ in Descending order (Correct)

    The candidates are ordered like this:
    - $(1, 4)$
    - $(1, 2)$
    
    We extract the $d$ values to find the Longest Non-Decreasing Subsequence: [4, 2].
    The algorithm looks at 4 and then 2. Since $2 < 4$, it cannot pick both.It can only pick 4 or 2, which means the subsequence length remains 1.
    This correctly enforces that we pick at most one candidate for the value $v = 1$.

4. Finally, since $v$ is already sorted, we find the Longest Non-Decreasing Subsequence on the $d$ values of our sorted candidates.

