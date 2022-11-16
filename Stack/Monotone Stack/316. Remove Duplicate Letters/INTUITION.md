## Monotonically and Lexicographcally Increasing Stack

key points:

1. stack is a perfect solution to help us check lexicographical order. we can use stack to check previous character (stack's top) with current character's lexicographical order easily
2. we can see that what we want is monotonically increasing. thus, we should use monotonic stack
3. Greedy
   1. if we've already has this character, don't bother it. because it can't be better if we preserve monotonically increasing stack until now. it's already best we can get
 
- we use two hashmap to track total character's count and current used character count.
- if current character is smaller than stack's top and we still has duplicate afterwards, we can safely pop stack's top to build better choice.
  - update `has` hashmap and don't forget to update total character's count.(our `counter`)
- if current character is greater than our monotonic stack, then we just append