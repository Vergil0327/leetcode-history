// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

package main

import (
	"fmt"
	"math"
)

// optimized way is to solve by math (combinatorics)
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/discuss/2527381/JavaC%2B%2BPython-Math-Solution-O(klogk)

func numberOfWays(startPos int, endPos int, k int) int {
	limit := int(7 + math.Pow10(9))

	interval := endPos - startPos
	if k > interval && (k-interval)%2 != 0 {
		return 0
	}

	if interval == k {
		return 1
	}

	memo := map[string]int{}

	var dfs func(start, end, k int, memo map[string]int) int
	dfs = func(start, end, k int, memo map[string]int) int {
		if k == 0 && start == end {
			return 1
		}

		if k == 0 {
			return 0
		}

		key := fmt.Sprintf("%d,%d,%d", start, end, k)
		if _, ok := memo[key]; ok {
			return memo[key]
		}

		memo[key] = (dfs(start+1, end, k-1, memo) + dfs(start-1, end, k-1, memo)) % limit
		return memo[key]
	}
	cnt := dfs(startPos, endPos, k, memo)

	return cnt % limit
}
