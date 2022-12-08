### INTUITION

這題主要利用的是，當一個array裡的數字正好符合index時，因為我們只要把每個數換到正確的位置上即可，如此一來可以用O(n)的時間去排序

首先我們在前面append一個位置，讓nums變成`1-based [1,n]` array

由於我們僅考慮在[1,n]間的未出現的最小正整數，所以我們可以忽略負數
並且我們要找的最小正整數勢必會出現在[1,n+1]這範圍內(nums.length)

例如nums=[1,2,3,4,5], 消失最小正整數為6
例如nums=[1,2,7,8], 消失最小正整數為3

再來我們把每個數根據他的值放到相對應的index位置的後，其實也就是對一個長度為n且值為1到n的array進行排序後(Indexing Sort, O(n))，我們只需要index從小到大遍歷，找出第一個val與index不符合的數即為答案

```
我們考慮範例1,2,3

example.1
一開始為[0,1,2,0]
對每個位置進行排序後: [0,1,2,0]
可得知消失的最小正整數為3，因為index=3時，value不為3

example.2 : [0,3,4,-1,1]
首先移除掉不合法的數:[0,3,4,0,1]
再來進行排序，將每個值放到相對應的index上
1st:[0,0,4,3,1]
2nd:[0,0,1,3,4]
3rd:[0,1,0,3,4]
由左往右遍歷可得知，消失的最小正整數為2

example.3: [0,7,8,9,11,12]
移除不合法的數值:[0,0,0,0,0,0]
可得知消失的最小正整數為1
```

ps. 這邊有個細節要注意

we can't use `nums[i], nums[nums[i]] = nums[nums[i]], nums[i]` to swap, because nums[i] is mutated in swap operation

nums[i], nums[nums[i]] = nums[nums[i]], nums[i] actually equals to:
```python
nums[i] = nums[nums[i]]
nums[nums[i]] = nums[i] # -> nums[i] has been updated, we'll swap with wrong position
```