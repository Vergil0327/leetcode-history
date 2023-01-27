# Intuition

let's see example 1:
like merge K sorted list, we can think each nums[j] as linked list and keep moving pointer of smallest nums[j][ptr] among all the nums and see current covered range. the minimum range should be answer

# Approach

thus, we can use minHeap to keep tracks of current minimum value among all the nums[j] where 0 <= j <= len(nums).

`minHeap = [value, pointer of nums[j], j]`

once we pop out minimum nums[j][ptr], we put nums[j][ptr+1] into minHeap and update range:

`range = [minHeap[0][0], max(ranges[1], nums[j][ptr+1])]`

```
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
0,4,5,   -> current covered range: [0,5]
pop out 0
4,5,9,   -> current covered range: [4,9]
pop out 4
5,9,10   -> current covered range: [5,10]
pop out 5
9,10,18  -> current covered range: [9,18]
pop out 9
12,15,18 -> current covered range: [12,18]
pop out 12
20,15,18 -> current covered range: [15,20]
pop out 15
20,24,18 -> current covered range: [18,24]
pop out 18
20,24,22 -> current covered range: [20,24]
20 is the end of nums[1] -> break
```

# Complexity

- time complexity
$$O(nlogn + mlogn)$$
where m is total num among all the nums and n is len(nums)

- space complexity

$$O(n)$$