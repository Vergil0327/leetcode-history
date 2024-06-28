# Intuition

j-i != nums[j]-nums[i]
=> j-nums[j] != i-nums[i]
=> convert nums to new arr = [i-nums[i] for i in range(n)]
=> 問題轉成找出兩pair (arr[i], arr[j]) 其中 arr[i] != arr[j] and j > i
=> iterate arr, res += (cnt := i) - count[arr[i]] => 相當於過往element數目 減去 與自身相同的element = 剩餘的合法element可組成bad pairs