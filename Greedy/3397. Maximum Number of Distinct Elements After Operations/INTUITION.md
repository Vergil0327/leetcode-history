# Intuition

直覺是先排序, 然後從nums[0]-k開始, 以greedy的方式, 持續放入盡可能最小但又剛好大於當前的最大distinct element

- 如果當前distinct array[-1] < nums[i]-k: 那我們就放入nums[i]-k
- 如果當前distinct array[-1] >= nums[i]-k: 那我們就看distinct array[-1]+1能不能透過操作轉換而來

持續放入最小合法數是為了讓後續有更多空間讓下個遍歷到的數能透過操作找出合法數

```py
nums.sort()

res = [nums[0]-k]
for i in range(1, len(nums)):
    if res[-1] < nums[i]-k:
        res.append(nums[i]-k)
    elif res[-1]+1 <= nums[i]+k:
        res.append(res[-1]+1)

return len(res)
```