### Union-Find

step by step:

1. union whenever equation is "a==b" where a, b is any lowercase character
2. check validity whenever equation is "a!=b" where a, b is any lowercase character
   1. if `isConnected(a, b)` is True, it violate `"a!=b"`. thus, we directly return False
   2. if all the equations are valid, return True