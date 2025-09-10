[C. Product of Three Numbers](https://codeforces.com/problemset/problem/1294/C)

time limit per test: 2 seconds
memory limit per test: 256 megabytes

You are given one integer number **𝑛**. Find three distinct integers 𝑎,𝑏,𝑐 such that 2≤𝑎,𝑏,𝑐 and 𝑎⋅𝑏⋅𝑐=𝑛 or say that it is impossible to do it.

If there are several answers, you can print any.

You have to answer 𝑡 independent test cases.

**Input**
The first line of the input contains one integer 𝑡 (1≤𝑡≤100) — the number of test cases.

The next 𝑛 lines describe test cases. The 𝑖-th test case is given on a new line as one integer 𝑛 (2≤𝑛≤$10^9$).

**Output**
For each test case, print the answer on it. Print "NO" if it is impossible to represent 𝑛 as 𝑎⋅𝑏⋅𝑐 for some distinct integers 𝑎,𝑏,𝑐 such that 2≤𝑎,𝑏,𝑐.

Otherwise, print "YES" and any possible such representation.

**Example**
Input
5
64
32
97
2
12345
Output
YES
2 4 8 
NO
NO
NO
YES
3 5 823 