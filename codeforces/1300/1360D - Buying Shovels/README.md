[D. Buying Shovels](https://codeforces.com/problemset/problem/1360/D)

time limit per test: 2 seconds
memory limit per test: 256 megabytes

Polycarp wants to buy exactly 𝑛 shovels. The shop sells packages with shovels. The store has 𝑘 types of packages: the package of the 𝑖-th type consists of exactly 𝑖 shovels (1≤𝑖≤𝑘). The store has an infinite number of packages of each type.

Polycarp wants to choose one type of packages and then buy several (one or more) packages of this type. What is the smallest number of packages Polycarp will have to buy to get exactly 𝑛 shovels?

For example, if 𝑛=8 and 𝑘=7, then Polycarp will buy 2 packages of 4 shovels.

Help Polycarp find the minimum number of packages that he needs to buy, given that he:

- will buy exactly 𝑛 shovels in total;
- the sizes of all packages he will buy are all the same and the number of shovels in each package is an integer from 1
 to 𝑘, inclusive.

**Input**
The first line contains an integer 𝑡 (1≤𝑡≤100) — the number of test cases in the input. Then, 𝑡 test cases follow, one per line.

Each test case consists of two positive integers 𝑛 (1≤𝑛≤$10^9$) and 𝑘 (1≤𝑘≤$10^9$) — the number of shovels and the number of types of packages.

**Output**
Print 𝑡 answers to the test cases. Each answer is a positive integer — the minimum number of packages.

**Example**
Input
5
8 7
8 1
6 10
999999733 999999732
999999733 999999733
Output
2
8
1
999999733
1

**Note**
The answer to the first test case was explained in the statement.

In the second test case, there is only one way to buy 8 shovels — 8 packages of one shovel.

In the third test case, you need to buy a 1 package of 6 shovels.