// https://leetcode.com/problems/meeting-rooms-iii/

package main

import (
	"container/heap"
	"sort"
)

// https://leetcode.com/problems/meeting-rooms-iii/discuss/2527548/Python-Heap-Solution
func mostBookedTwoHeap(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	roomReady := MinHeapInt([]int{}) // room
	roomInUsed := MinHeap([][]int{}) // [room, endTime]
	count := map[int]int{}

	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]

		// clean finished room
		for roomInUsed.Len() > 0 && roomInUsed[0][1] < start {
			item := heap.Pop(&roomInUsed).([]int)
			heap.Push(&roomReady, item)
		}

		if roomReady.Len() > 0 {
			room := heap.Pop(&roomReady).(int)
			heap.Push(&roomInUsed, []int{room, end})
			count[room] += 1
		} else {
			item := heap.Pop(&roomInUsed).([]int)
			room, finish := item[0], item[1]
			heap.Push(&roomInUsed, []int{room, finish + end - start})
			count[room] += 1
		}
	}

	maxIdx := 0
	for i := 0; i < n; i++ {
		if count[i] > count[maxIdx] {
			maxIdx = i
		}
	}

	return maxIdx
}

// nLog(n)
func mostBookedBetterFindMaxFreq(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	h := MinHeap([][]int{}) // [room, endTime]
	for i := 0; i < n; i++ {
		h = append(h, []int{i, 0})
	}
	heap.Init(&h)

	count := map[int]int{}
	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]

		// clean room
		for h.Len() > 0 && h[0][1] < start {
			item := heap.Pop(&h).([]int)
			heap.Push(&h, []int{item[0], start})
		}

		item := heap.Pop(&h).([]int)
		room := item[0]
		finish := item[1]
		if finish > start {
			end = finish + end - start
		}

		count[room] += 1
		heap.Push(&h, []int{room, end})
	}

	maxIdx := 0
	for i := 0; i < n; i++ {
		if count[i] > count[maxIdx] {
			maxIdx = i
		}
	}

	return maxIdx
}

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	h := MinHeap([][]int{}) // [room, endTime]
	for i := 0; i < n; i++ {
		h = append(h, []int{i, 0})
	}
	heap.Init(&h)

	count := map[int]int{}
	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]

		// clean room
		for h.Len() > 0 && h[0][1] < start {
			item := heap.Pop(&h).([]int)
			heap.Push(&h, []int{item[0], start})
		}

		item := heap.Pop(&h).([]int)
		room := item[0]
		finish := item[1]
		if finish > start {
			end = finish + end - start
		}

		count[room] += 1
		heap.Push(&h, []int{room, end})
	}

	ans := [][]int{}
	for room, used := range count {
		ans = append(ans, []int{room, used})
	}

	sort.Slice(ans, func(i, j int) bool {
		if ans[i][1] == ans[j][1] {
			return ans[i][0] < ans[j][0]
		}
		return ans[i][1] > ans[j][1]
	})
	return ans[0][0]
}

type MinHeap [][]int // room

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	if h[i][1] == h[j][1] {
		return h[i][0] < h[j][0]
	}

	return h[i][1] < h[j][1]
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.([]int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type MinHeapInt []int // [room, endTime]

func (h MinHeapInt) Len() int {
	return len(h)
}
func (h MinHeapInt) Less(i, j int) bool {

	return h[i] < h[j]
}
func (h MinHeapInt) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeapInt) Push(item interface{}) {
	*h = append(*h, item.(int))
}
func (h *MinHeapInt) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
