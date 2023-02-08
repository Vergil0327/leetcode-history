# 5D DP

## Intuition
雖然 python 會TLE，但這應該是最正規的解法了

首先可以看到m, n的範圍很小，每一行的分數僅受上一行影響且也僅影響上一行
因此可以用bitmask的概念進行狀態壓縮，每一格能有三種狀態`沒人`, `introvert`, `extrovert`

所以這樣一行會有3**n種狀態，n最多為`5`，也就是243，因此dp[row][state]則為`m*(3**n)`，算是可接受狀態

狀態轉移的框架大概會是:
```py
for row in range(m):
    for state in range(3**n):
        for prevState in range(3**n):
            dp[row][state] = max(dp[row][state], dp[row-1][prevState] + computeScore(prevState, state))
```

但由於introvert和extrovert的人數也有限制，所以我們也必須記錄我們每個狀態是不是合理的，如果超出人數限制那麼這狀態轉移應該是無效的

因此dp的狀態應該增加為`dp[row][state][# of introvert][# of extrovert]`，然後對於每個狀態都該檢查introvert及extrovert的人數，因此都要遍歷一遍，因此狀態轉移就會變成
```py
for row in range(m):
    for intro in range(introvert+1):
        for extro in range(extrovert+1):
            for state in range(3**n):
                curIntro, curExtro = countPeopleState(state)
                if curIntro > intro or curExtro > extro: continue # invalid state
                for prevState in range(3**n):
                    dp[row][state][introv][extro] = max(dp[row][state][introv][extro], dp[row-1][prevState] + computeScore(prevState, state))
                if row == m-1:
                    res = max(res, dp[row][state][intr][extr])
```
那最終的答案就是在dp[m-1]裡的所有狀態找最大值，由於introvert, extrovert跟state的任何可能都可能是最佳解，因此需要全部遍歷一遍

```py
ans = -inf
for intro in range(introvert+1):
    for extro in range(extrovert+1):
        for state in range(3**n):
            ans = max(ans, dp[m-1][state][intro][extro])
```

或者我們直接在更新狀態時，在row == m-1的時候同步更新`ans`

**注意事項**
1. 我們將row改成1-indexed，然後由於我們是要取max，因此dp初始值設為`-inf`，那這樣base case:
`dp[0][0][0][0]=0`

2. `countPeopleType`就單純找出目前`state`裡有幾個introvert及extrovert

3. 比較要注意的是`computeScore`

對於current state來說，除了要看周遭人來決定分數以外
我們還要記得計算current state對prevState的影響，也就是:

```py
# 如果current state第i位有人的話，prevState的分數影響也該算進去
if currentState[i] == introvert or currentState[i] == extrovert:
    if prevState[i] == introvert: # prevState[i]有個introvert，
        happy -= 30
    elif prevState[i] == extrovert:
        happy += 20
```

## Optimized Solution

可惜的是python會超時，因此另外有個更精妙的算法為輪廓線DP，有點像是將狀態壓縮成一個sliding window，而非單純的bitmask

```java
// Link: https://leetcode.com/problems/maximize-grid-happiness/solutions/936256/java-detailed-explanation-5d-dp-ternary-base-3-state-compression

public int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        
	return helper(m, n, 0, 0, introvertsCount, extrovertsCount, 0,
				  new Integer[m][n][introvertsCount + 1][extrovertsCount + 1][243]);
}

// Ternary get ith bit value (0, 1 or 2)
private int get(int prevN, int i) {
	prevN /= ((int) Math.pow(3, i));
	return prevN % 3;
}

// Ternary set new-coming bit to value
private int set(int currRow, int value) {
	return (currRow * 3 + value) % 243;
}

// Ternary bit meaning -> empty: 0, intro: 1, extro: 2
private int helper(int m, int n, int x, int y, int iCount, int eCount, 
				   int prevN, Integer[][][][][] dp) {

	// advance pointer
	if (y == n) {
		y = 0;
		x++;
	}

	if (iCount == 0 && eCount == 0) return 0;

	if (x == m) return 0;

	if (dp[x][y][iCount][eCount][prevN] != null) return dp[x][y][iCount][eCount][prevN];

	// leave the cell empty
	int res = helper(m, n, x, y + 1, iCount, eCount, set(prevN, 0), dp);

	int up = get(prevN, n - 1);  // get up bit -> which is at (n - 1)th
	int left = get(prevN, 0);  // get left bit -> which is at (0)th

	if (iCount > 0) {  // put intro guy at current cell

		int temp = prevN;
		prevN = set(prevN, 1);  // set new-coming bit to 1

		int addOn = 120;

		if (x - 1 >= 0 && up != 0) {
			addOn -= 30;
			if (up == 1) addOn -= 30;
			else addOn += 20;
		}

		if (y - 1 >= 0 && left != 0) {
			addOn -= 30;
			if (left == 1) addOn -= 30;
			else addOn += 20;
		}

		res = Math.max(res, helper(m, n, x, y + 1, iCount - 1, eCount, prevN, dp) + addOn);

		prevN = temp;  // set it back
	}

	if (eCount > 0) {  // put extro guy at current cell

		int temp = prevN;
		prevN = set(prevN, 2);  // set new-coming bit to 2

		int addOn = 40;

		if (x - 1 >= 0 && up != 0) {
			addOn += 20;
			if (up == 1) addOn -= 30;
			else addOn += 20;
		}

		if (y - 1 >= 0 && left != 0) {
			addOn += 20;
			if (left == 1) addOn -= 30;
			else addOn += 20;
		}

		res = Math.max(res, helper(m, n, x, y + 1, iCount, eCount - 1, prevN, dp) + addOn);

		prevN = temp;  // set it back
	}

	return dp[x][y][iCount][eCount][prevN] = res;
}
```
```py
# 輪廓線 DP
# 作者：zerotrac2
# 链接：https://leetcode.cn/problems/maximize-grid-happiness/solution/zui-da-hua-wang-ge-xing-fu-gan-by-zerotrac2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        # 如果 x 和 y 相邻，需要加上的分数
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0:
                return 0
            # 例如两个内向的人，每个人要 -30，一共 -60，下同
            if x == 1 and y == 1:
                return -60
            if x == 2 and y == 2:
                return 40
            return -10
        
        n3 = 3**n
        # 预处理：每一个 mask 的三进制表示
        mask_span = dict()
        # 预处理：每一个 mask 去除最高位、乘 3、加上新的最低位的结果
        truncate = dict()

        # 预处理
        highest = n3 // 3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask % highest * 3,
                mask % highest * 3 + 1,
                mask % highest * 3 + 2,
            ]
        
        # dfs(位置，轮廓线上的 mask，剩余的内向人数，剩余的外向人数)
        @lru_cache(None)
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            # 边界条件：如果已经处理完，或者没有人了
            if pos == m * n or nx + wx == 0:
                return 0
            
            x, y = divmod(pos, n)
            
            # 什么都不做
            best = dfs(pos + 1, truncate[borderline][0], nx, wx)
            # 放一个内向的人
            if nx > 0:
                best = max(best, 120 + calc(1, mask_span[borderline][0]) \
                                     + (0 if y == 0 else calc(1, mask_span[borderline][n - 1])) \
                                     + dfs(pos + 1, truncate[borderline][1], nx - 1, wx))
            # 放一个外向的人
            if wx > 0:
                best = max(best, 40 + calc(2, mask_span[borderline][0]) \
                                    + (0 if y == 0 else calc(2, mask_span[borderline][n - 1])) \
                                    + dfs(pos + 1, truncate[borderline][2], nx, wx - 1))

            return best
        
        return dfs(0, 0, nx, wx)
```