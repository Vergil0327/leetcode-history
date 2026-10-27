[4090. Count Magical Substring Pairs I](https://leetcode.com/problems/count-magical-substring-pairs-i/)

`Medium`

You are given a string s of length n consisting of lowercase English letters.

For every triplet of indices (i, j, k) satisfying 0 <= i <= j < k < n, define:

- s1 = s[i..j]
- s2 = s[j + 1..k]
A pair of substrings (s1, s2) is called magical if the number of distinct characters in s1 is equal to the number of distinct characters in s2.

Return the number of triplets (i, j, k) for which (s1, s2) is a magical pair.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "aba"
Output: 2
Explanation:

There are 2 valid triplets:

No.	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
1	(0, 0, 1)	"a"	"b"	1	1
2	(1, 1, 2)	"b"	"a"	1	1

Example 2:
Input: s = "kkk"
Output: 4
Explanation:
There are 4 valid triplets:

No.	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
1	(0, 0, 1)	"k"	"k"	1	1
2	(0, 0, 2)	"k"	"kk"	1	1
3	(0, 1, 2)	"kk"	"k"	1	1
4	(1, 1, 2)	"k"	"k"	1	1

Example 3:
Input: s = "abcac"
Output: 7
Explanation:
There are 7 valid triplets:

No.	(i, j, k)	s1	s2	distinct(s1)	distinct(s2)
1	(0, 0, 1)	"a"	"b"	1	1
2	(1, 1, 2)	"b"	"c"	1	1
3	(2, 2, 3)	"c"	"a"	1	1
4	(3, 3, 4)	"a"	"c"	1	1
5	(0, 1, 3)	"ab"	"ca"	2	2
6	(0, 1, 4)	"ab"	"cac"	2	2
7	(1, 2, 4)	"bc"	"ac"	2	2

Constraints:

- 2 <= s.length <= 2000
- s consists of lowercase English letters.

Accepted
10,697/23.9K
Acceptance Rate
44.8%
