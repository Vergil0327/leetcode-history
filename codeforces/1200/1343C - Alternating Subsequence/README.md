[C. Alternating Subsequence](https://codeforces.com/problemset/problem/1343/C)

time limit per test: 1 second
memory limit per test: 256 megabytes

Recall that the sequence 𝑏 is a a subsequence of the sequence 𝑎 if 𝑏 can be derived from 𝑎 by removing zero or more elements without changing the order of the remaining elements. For example, if 𝑎=[1,2,1,3,1,2,1], then possible subsequences are: [1,1,1,1], [3] and [1,2,1,3,1,2,1], but not [3,2,3] and [1,1,1,1,2].

You are given a sequence 𝑎 consisting of 𝑛 positive and negative elements (there is no zeros in the sequence).

Your task is to choose maximum by size (length) alternating subsequence of the given sequence (i.e. the sign of each next element is the opposite from the sign of the current element, like positive-negative-positive and so on or negative-positive-negative and so on). Among all such subsequences, you have to choose one which has the maximum sum of elements.

In other words, if the maximum length of alternating subsequence is 𝑘 then your task is to find the maximum sum of elements of some alternating subsequence of length 𝑘.

You have to answer 𝑡 independent test cases.

Input
The first line of the input contains one integer 𝑡 (1≤𝑡≤$10^4$) — the number of test cases. Then 𝑡 test cases follow.

The first line of the test case contains one integer 𝑛 (1≤𝑛≤2⋅$10^5$) — the number of elements in 𝑎. The second line of the test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (−$10^9$≤𝑎𝑖≤$10^9$,𝑎𝑖≠0), where 𝑎𝑖 is the 𝑖-th element of 𝑎.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅$10^5$ (∑𝑛≤2⋅$10^5$).

Output
For each test case, print the answer — the maximum sum of the maximum by size (length) alternating subsequence of 𝑎.

Example
Input
4
5
1 2 3 -1 -2
4
-1 -2 -1 -3
10
-2 8 3 8 -4 -15 5 -2 -3 1
6
1 -1000000000 1 -1000000000 1 -1000000000
Output
2
-1
6
-2999999997

Note
In the first test case of the example, one of the possible answers is [1,2,3⎯⎯,−1⎯⎯⎯⎯⎯,−2].

In the second test case of the example, one of the possible answers is [−1,−2,−1⎯⎯⎯⎯⎯,−3].

In the third test case of the example, one of the possible answers is [−2⎯⎯⎯⎯⎯,8,3,8⎯⎯,−4⎯⎯⎯⎯⎯,−15,5⎯⎯,−2⎯⎯⎯⎯⎯,−3,1⎯⎯].

In the fourth test case of the example, one of the possible answers is [1⎯⎯,−1000000000⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯,1⎯⎯,−1000000000⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯,1⎯⎯,−1000000000⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯].