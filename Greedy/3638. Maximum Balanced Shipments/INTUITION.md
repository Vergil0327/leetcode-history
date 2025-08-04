# Intuition

記錄`nums[:i)`當前的max element, 並以greedy方式去找出符合`nums[i] < max element`的合法subarray
一旦符合, 就在往後重新找下一個合適的

max element只會越找越大, 並且一旦找到符合的nums[i]就結算, 後面nums[i+1:]能繼續找到合法的subarray機率也越高
所以就以greedy方式去找即可