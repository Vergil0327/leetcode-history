[B. Ilya and Queries](https://codeforces.com/problemset/problem/313/B)

time limit per test2 seconds
memory limit per test256 megabytes

Ilya the Lion wants to help all his friends with passing exams. They need to solve the following problem to pass the IT exam.

You've got string s = s1s2... sn (n is the length of the string), consisting only of characters "." and "#" and m queries. Each query is described by a pair of integers li, ri (1 ≤ li < ri ≤ n). The answer to the query li, ri is the number of such integers i (li ≤ i < ri), that si = si + 1.

Ilya the Lion wants to help his friends but is there anyone to help him? Help Ilya, solve the problem.

Input
The first line contains string s of length n (2 ≤ n ≤ 105). It is guaranteed that the given string only consists of characters "." and "#".

The next line contains integer m (1 ≤ m ≤ 105) — the number of queries. Each of the next m lines contains the description of the corresponding query. The i-th line contains integers li, ri (1 ≤ li < ri ≤ n).

Output
Print m integers — the answers to the queries in the order in which they are given in the input.

Examples
Input
......
4
3 4
2 3
1 6
2 6
Output
1
1
5
4
Input
#..###
5
1 3
5 6
1 5
3 6
3 4
Output
1
1
2
2
0
