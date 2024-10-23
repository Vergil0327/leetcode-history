# Intuition

思路很直覺:
1. 由於我們需要`pushFront`跟`pushBack`, 所以我們需要`deque`這數據結構
2. 由於我們還需要`pushMiddle`, 所以我們從中間切開, 維護兩個`deque`
   - 假如兩邊size不一直, 我們統一維護將middle element放在左邊

3. 那再來就只需要在`pushFront`, `pushBack`跟`pushMiddle`的過程中, 同時維護兩個`deque`的size即可, 讓他們始終保持著`left_deque.size <= right_deque.size+1`

ex. 
left = [XX], right = [OO]
left = [XX], right = [O]

4. 注意如果deque為空, 我們得返回`-1`

那這樣:

time complexity per method: O(1)