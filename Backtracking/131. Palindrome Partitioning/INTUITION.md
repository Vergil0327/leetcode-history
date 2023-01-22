# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
split s into two substring `left` and `right`
if `left` is palindrome, keep backtracking rest of substring `right`

if we successfully split `s` into many palindromes, `s` will be empty string and this is our base case

# Complexity

- Time Complexity

$$O(N⋅2^N)$$
, where N is the length of string s. This is the worst-case time complexity when all the possible substrings are palindrome.
Example, if s is aaa, the recursive tree can be illustrated as follows:

![time_complexity](time_complexity.png)

Hence, there could be $2^N$ possible substrings in the worst case. For each substring, it takes O(N) time to generate the substring and determine if it is a palindrome or not. This gives us a time complexity of $O(N⋅2^N)$

- Space Complexity

O(N), where N is the length of the string s. This space will be used to store the recursion stack. For s = aaa, the maximum depth of the recursive call stack is 3 which is equivalent to N.