package main

import "sort"

func carPooling(trips [][]int, capacity int) bool {
	start := [][2]int{}
	end := [][2]int{}
	for _, trip := range trips {
		start = append(start, [2]int{trip[1], trip[0]})
		end = append(end, [2]int{trip[2], trip[0]})
	}

	sort.Slice(start, func(i, j int) bool {
		return start[i][0] < start[j][0]
	})
	sort.Slice(end, func(i, j int) bool {
		return end[i][0] < end[j][0]
	})

	i, j := 0, 0
	currCap := 0
	for i < len(start) {
		if start[i][0] < end[j][0] { // pick-up
			currCap += start[i][1]
			i += 1
		} else { // drop-off
			currCap -= end[j][1]
			j += 1
		}

		if currCap > capacity {
			return false
		}
	}
	return true
}
