// https://leetcode.com/problems/minimum-interval-to-include-each-query/
package main

import (
	"container/heap"
	"sort"
)

/*
there is also a special clever solution by using Union-Find
https://leetcode.com/problems/minimum-interval-to-include-each-query/discuss/1186840/Python-union-find
*/

// explanation: https://www.youtube.com/watch?v=5hQ5WWW5awQ
// Time O(nlog(n) + qlog(q))
// Space O(n+q)
func minInterval(intervals [][]int, queries []int) []int {
	// T:O(nLog(n))
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	origQueries := make([]int, len(queries))
	copy(origQueries, queries)

	// T:O(qLog(q))
	sort.Slice(queries, func(i, j int) bool {
		return queries[i] < queries[j]
	})

	res := make([]int, len(queries))
	minH := MinHeap([]Interval{})
	ans := make(map[int]int)

	for _, q := range queries {
		// T:O(log(n))
		for len(intervals) > 0 && intervals[0][0] <= q {
			interval := intervals[0]
			heap.Push(&minH, Interval{left: interval[0], right: interval[1], size: interval[1] - interval[0] + 1})
			intervals = intervals[1:]
		}

		// T:O(lon(n)), remove invalid interval
		for minH.Len() > 0 && minH[0].right < q {
			heap.Pop(&minH)
		}

		// T:O(1)
		if minH.Len() > 0 {
			ans[q] = minH[0].size
		} else {
			ans[q] = -1
		}
	}

	// T:O(q)
	for i, q := range origQueries {
		res[i] = ans[q]
	}

	return res
}

type Interval struct {
	size, left, right int
}

type MinHeap []Interval

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	// !!! tie-breaker
	if h[i].size == h[j].size {
		return h[i].right < h[j].right // we gonna pop out invalid interval by right value later
	}

	return h[i].size < h[j].size
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(Interval))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
