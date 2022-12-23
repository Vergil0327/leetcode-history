# Top-Down DP

## Intuition

let's see our decision tree:

1. jump forward
   1. only can jump to `i+x` where `0 < x <= d`
   2. `arr[i+x]` must be minimum value within [i:i+x] (both inclusive). i.e. arr[i+x] where `0<x<=d` must be monotonically decreasing.

2. jump backward
   1. only can jump to `i-x` where `0 < x <=d`
   2. `arr[i-x]` must be minimum value within [i-x:i] (both inclusive). i.e. arr[i-x] where `0<x<=d` must be monotonically decreasing.

- we don't want to jump back and forth. thus, we need a `visited` hashset

- we can see that we don't need to re-compute every result. when we compute **jumping from A to C to B**, we've already computed **jumping from C to B**

that's all we need to write DFS.

## Optimized

in fact, we don't need `visited` hashset because it's impossible to jump back and forth based on the constraint of monotonically decreasing value.

we can only jump to strictly lower place, therefore, we can get rid of `visited` hashset

## Complexity

- time complexity:
$$O(d*N)$$

- space complexity:
$$O(n)$$

## Further Reading

the optimal time complexity of this problem is **O(n)**.

see [here](https://leetcode.com/problems/jump-game-v/solutions/498379/python-concise-actual-o-n-monotone-stacks-dfs-also-188ms-beats-100/)

```python
import functools

class Solution:
    def maxJumps(self, A, d):
        N = len(A)
        graph = collections.defaultdict(list)
        
        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i - j) <= d: graph[j].append(i)
                stack.append(i)
        
        jump(range(N))
        jump(reversed(range(N)))
        
        @functools.lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)
        
        return max(map(height, range(N)))
```