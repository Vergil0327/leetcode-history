# Intuition

有點像是leetcode另道題目, 模擬加減乘除計算機運算那樣

首先很明顯能看到的是, 我們的目標是透過
1. 遞歸
2. 或Stack
, 從外層一層層的剝掉{}後, 在處理裡面的sub-problem


- {}{}:相當於乘法
- ",": 相當於加法
- 同時每個操作後都必須透過hashset去除duplicate

ex. {x, x, x, x, x}{y,y,y}
{x, x, x, x, x} => 剝掉後 => x,x,x,x,x => 我們返回[[x],[x],[x],[x],[x]]
這樣才方便跟後續剝掉的{y,y,y} = [[y],[y],[y]]進行乘法形成: {xy,xy,xy, ...}
然後再透過hashset去除duplicate

再來`"{}"`相當於四則運算的括號 => stack 或 recursion

而在遇到`","`運算符時, 前後array則是要拼接起來
所以stack裡面維護的每個element必須是個array, 代表的是同一層級括號內的每個元素

另外`a{x, y}`, 我們可以視為`{a}{x,y}`這是等價的
所以根據前面: a{x,y} = {a}{x,y} = product([a], [x,y]) = [ax, ay]

那這樣我們可以開始用iterative的方式, 透過`stack`來剝除括號
並用`arr`, `cur`維護當前level
- arr: `","`的前一個array
- cur: 當前處理的array

接下來討論expr[i]遇到運算符或是字母時的操作:
1. **if expr[i].isalpha()**: expr[i]跟當前level的當前array相乘積
   - `cur = product(cur, [expr[i]])`
2. **if expr[i] == "{"**: 當前加入stack, 然後新處理下一個level
   - stack.append(arr)
   - stack.append(cur)
   - arr, cur = [], []
3. **if expr[i] == "}"**: pop掉當前level, 並於上層level的最後一個array相乘積
   - 當前level為: arr + cur
   - 上層level array為:
     - preCur = stack.pop()
     - preArr = stack.pop()
     - cur = product(preCur, arr+cur)
     - arr = preArr
4. **if expr[i] == ","**: 前後array拼接在一起
   - arr += cur
   - cur = []

最後結果就是`arr+cur`, 我們在加入hashset裡並排序即得答案

# Complexity

- time complexity: $O(n + nlogn)$