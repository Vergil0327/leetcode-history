# Intuition

首先想到**Brute Force**
找一個中間點往前往後暴力搜索出所有可能seg然後XOR出max value

time: O(n * (n*k + 2^7 * 2^7))
space: O(n*k)