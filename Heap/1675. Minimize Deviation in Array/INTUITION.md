# Intuition

if we can optimize $$deviation$$, we must need to decrease maximum num or increase minimum num

it's hard to deal with increase minimum value by `*=2` or  decrease maximum value by `//= 2` at the same time, so I try to handle it separately.

> first of all, we can know that:
> MX = max(nums)
> MN = min(nums)
> $$deviation = MX-MN$$ # default value

ok, then I decide to try every possiblilities since I can't come up with a super cool algorithm to solve.

first, let's try to increase every minimum possible value and see if we can optimize our $$deviation$$

since we want to find current minimum value after we increase it, we can use `Min Heap` to help us.

- precondition: minimum num must be **odd**
- if minimum num after increasing `<` **MX**, we can safely push to min heap and try to optimize $$deviation$$ by `MX-minHeap[0]`
- if minimum num after increasing `>=` **MX**, we can update our **MX** and push increased num to min heap and try to optimize $$deviation$$

then again, let's try to decrease maximum value and see if we can optimize our $$deviation$$.

the logic is same as above, this time we use **Max Heap** to find currently maximum num after each operation.

- precondition: maximum num must be **even**
- if maximum num after decreasing `>` **MN**, we can safely push back to max heap and try to optimize $$deviation$$ by `maxHeap[0]-MN`
- if maximum num after decreasing `<=` **MN**, update **MN**, push back to min heap and try to optimzie $$deviation$$

# Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$

# Other Solution 1

Logic is similar to ours but only use one **Max Heap**

add every num to max heap and if it's a odd number, inrease it by `*=2`.
afterwards, if we can optimize our $$deviation$$, we can only decrease maximum num by `//=2` if maximum num is **even**

```py
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            if num % 2 == 0:
                num = -num
            else:
                num = -num * 2
            heapq.heappush(max_heap, num)

        min_dev = float('inf')
        min_val = -max(max_heap)

        while len(nums) == len(max_heap):
            curr = -heapq.heappop(max_heap)
            min_dev = min(min_dev, curr-min_val)
            if curr % 2 == 0:
                min_val = min(min_val, curr//2)
                heapq.heappush(max_heap, -curr//2)
            else:
                break
        
        return min_dev
```

