# Intuition

find maximum number of achievable requests
=> 要形成achievable requests代表人數的移動必須成一個cycle (directed graph)
=> 我們要找到`max(sum(cycle size))`

如果example 1的x, y少任意一個的話, 就會變成兩個cycle二選一
這時當然選擇`building 0 -> building -> 1 -> building 2 -> building 0`這個cycle而非`building 1 <-> building 0`

當時就這裡卡住, 以為是要以graph的方式去想, 但實際上這題要求的是取任意subset of request
然後看他是不是都可以是合法的cycle, 也就是全部淨移動為0

由於數據規模很小, 只有`1 <= requests.length <= 16`, 所以可以用bitmask來暴力枚舉所有選取的狀態

我們就看當前枚舉的選取狀態的淨移動, 是不是可以讓每個building的人移動完後各building人數依然不變
如果是, 代表這是個合法的選取, 此時就可以更新`res = max(res, countOneBit(state))`

我們遍歷所有可能選取狀態, 這樣時間會是2^(len(requests)), 計算當前state.size會是O(len(requests))
因此時間複雜度為`O(2^m * m) where m is requests.size`

# Other Solution

同樣地, 也能用backtracking的方式再加上 take-or-skip 來看每個選取狀態是不是合法
合法就更新res