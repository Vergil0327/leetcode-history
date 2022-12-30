# Deque

## Intuition

first, let's split version1 and version2 and put them into deque

afterwards, we compare digit by digit

there are 4 cases:

1. both of them are empty at the same time: return 0 because they are equal
2. version1 is empty or version2 is empty
  - if version1 is empty, we need to check if the rest of version of version2 is greater than 0
    - if it's greater than 0, return -1
    - else they are equal. return 0
  - if version2 is empty, check if rest of version fo version1 is greater than 0
    - if it is, return 1
    - else return 0

    ```
    ex version1 = 1.0.1, version2 = 1
    ans: 1 because version1 > version2
    ```
3. both of them are not empty, compare digit by digit normally. if they are equal, continue to compare next digit

## Complexity

- time complexity

$$O(mn)$$

, where m is length of version1 and n is length of version2

- space complexity

$$O(mn)$$

, where m is length of version1 and n is length of version2