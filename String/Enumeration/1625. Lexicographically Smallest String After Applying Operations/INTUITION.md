# Intuition

op1: add `a` to all odd index and digit becomes (s[odd_idx] + a)%10
op2: rotate s by `b` position => move s[i] to s[(i+b)%n] where n = len(s)

maybe use dfs to explore?
1. with operation1, in worst case we have 10 strings due to "add a" operation;
2. With operation2, for each string in step 1, in worst case we can have n new strings, where n = s.length();
    - For each string, if b is odd, in worst case we can create 10 strings due to "add a" operation;
    - if b is even, then no new strings can be created during this step
therefore, the time and space complexity is O(10 * n * 10)
