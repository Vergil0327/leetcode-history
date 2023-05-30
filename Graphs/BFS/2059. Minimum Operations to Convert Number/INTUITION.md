# Intuition

對於合法範圍內的x來說 (0 <= x <= 1000)
他下個狀態都很清楚地告知了
1. x can `+nums[i]`
2. x can `-nums[i]`
3. x can `^nums[i]`
   - 注意只有當`nums[i] > 0`時才能進行 XOR 操作

因此對於要搜尋最短路徑來說, 我們可以用BFS來找所需步驟
為了避免重複, 記得用**hashset**紀錄我們獲得過的每個`x`