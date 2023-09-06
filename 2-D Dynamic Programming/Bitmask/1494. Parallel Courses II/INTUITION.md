# Intuition

first, I think we can use topological sort to take course.
one semester for k course which means strip off k nodes, and we just count how many semester we need to strip off all the nodes by topological sort
just like strip off onion, strip from outer to inner

since we can parallelly strip off if we've done all the prerequisites in the **previous** semester

ex.
if we have 2 courses, A and B, and their prerequisite < k,
one course, A, can be taken in next semester since we can take all the prerequisite in this semester.
thus, next semester we can continue to take remain prerequisite courses of B in previous semester and new course A in this semester.

what if we have multiple course path? what kind of way should we pick the available course?

ex.
```
1->2->..
3->4->..
5->6->..
```

therefore, we should try all possible way to take courses and find minimum because I think there is no greedy way to take courses.

see constraints: `1 <= n <= 15`

- we can use bitmask to represent the course we take or not. ex. `1001` means course 1 and course 4 has already been taken.
- then we can use top-down dp (dfs) or bottom-up with bitmask to explore all possibilities
- if use top-down dp, the depth of dfs is our required semesters, and we choose globally minimum


## bottom-up

high-level overview:

```py
for state in range(1<<n):

    """
    if we want update dp from prevState to state, it's valid when:
    1. prevState is a substate of state
    2. state.bit_count() - prevState.bit_count() <= k
    3. prevState must contain prerequisites of state
    """

    dp[state] = min(dp[state], dp[prevState]+1)
```

[detail explanation by HuifengGuan](https://www.youtube.com/watch?v=g2jmxEzwtv0&ab_channel=HuifengGuan)