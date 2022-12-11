# Array & Hashing
## Intuition
- use hashmap to store length of every Square Streak Seq.

## Approach

sort the array in decreasing order, and use hashset to remove duplicate num.

```
Square Streak Seq. of [2, 4, 4, 16] is [2,4,16] and length is 3
when we compute length of Square Streak Seq., we don't want to count 4 twice
```

iterate through `nums`, if we haven't seen this num before, store it in hashmap.
it's the head of `Square Streak Sequence` and we use it as key in hashmap.

continue iterating:
if current num's square exists in hashmap, find its sequence head and increment count

after we finish iteration, we return largest value in hashmap if its count is greater than 1 (sequence length must be 2 at least).

## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$

# DP

[original post](https://leetcode.com/problems/longest-square-streak-in-an-array/solutions/2899678/short-dp-c-java-lis-type/?orderBy=most_votes)

## Intuition

For every number we reach, we just check if its a **perfect square**:
- If its a Perfect Square, we pair up with its Square Root.
- Else, we keep it in dp array with length as 1, for pairing up its square number later.

## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$


```java
public int longestSquareStreak(int[] A) {
    HashMap<Integer, Integer> dp = new HashMap<>();
    int res = 0;
    Arrays.sort(A);
    for(var i : A) {
        int root = (int)Math.sqrt(i);
        if(root * root == i) {
          dp.put(i, dp.getOrDefault(root, 0) + 1);
        } else {
          dp.put(i, 1);
        }
        res = Math.max(res, dp.get(i));
    }
    return res < 2 ? -1 : res;
}
```