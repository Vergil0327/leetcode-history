# Intuition

1. use stack to handle `..` operator. `..` means go up to parent directory, therefore, we can simulate this by popping out item from stack if stack is not empty
2. skip `.` operator or empty string.
   - ex. `"//".split("/")` will generate `""`
3. append valid directory to stack and re-compose path after above steps

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$