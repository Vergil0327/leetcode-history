just like [leetcode 236](../236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree/)

we maintain a **cnt** variable to judge if we meet both `p` & `q` in the end
- if we meet `p` or `q`, increment **cnt** by 1
- if our **cnt** == 2, it means we meet both `p` & `q` during recursion
- if our **cnt** < 2, it means this binary tree is lack of `p` or `q` or both