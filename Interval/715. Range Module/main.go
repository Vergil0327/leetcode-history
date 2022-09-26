package main

// explanation: https://www.youtube.com/watch?v=pcpB9ux3RrQ
type RangeModule struct {
	intervals [][]int // [left, right)
}

func Constructor() RangeModule {
	return RangeModule{
		intervals: make([][]int, 0),
	}
}

func (this *RangeModule) AddRange(left int, right int) {
	tmp := [][]int{}

	inserted := false
	for _, interval := range this.intervals {
		if interval[0] > right && !inserted {
			tmp = append(tmp, []int{left, right})
			inserted = true
		}

		start, end := interval[0], interval[1]

		// no overlap
		if end < left || start > right {
			tmp = append(tmp, interval)
		} else {
			// merge interval
			// left < end && right > start
			//          start-------end
			//      left  -----right
			// start--------end
			left = min(left, start)
			right = max(right, end)
		}
	}

	// empty this.intervals || []int{left, right} at last position
	if !inserted {
		tmp = append(tmp, []int{left, right})
	}

	this.intervals = tmp
}

func (this *RangeModule) QueryRange(left int, right int) bool {
	l, r := 0, len(this.intervals)-1
	for l <= r {
		mid := l + (r-l)/2

		if this.intervals[mid][1] < left {
			l = mid + 1 // 排除不可能, this.intervals[mid][1] < left 這區間不是我們要找的
		} else if this.intervals[mid][0] > right {
			r = mid - 1 // 排除不可能, this.intervals[mid][0] > right 這區間不是我們要找的
		} else {
			interval := this.intervals[mid]
			return interval[0] <= left && interval[1] >= right
		}
	}

	return false
}

func (this *RangeModule) RemoveRange(left int, right int) {
	tmp := [][]int{}

	for _, interval := range this.intervals {
		start, end := interval[0], interval[1]
		// no overlapping
		if end <= left || start >= right {
			tmp = append(tmp, interval)
		} else {
			//        left ------------- right
			//                   start --------- end
			//             start -- end <- don't append
			// start --------- end
			// start ---------------------------- end
			// we want [start, left] || [right, end]

			if start < left {
				tmp = append(tmp, []int{start, left})
			}
			if right < end {
				tmp = append(tmp, []int{right, end})
			}
		}
	}

	this.intervals = tmp
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}

	return b
}
