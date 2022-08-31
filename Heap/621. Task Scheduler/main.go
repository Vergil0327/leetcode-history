// https://leetcode.com/problems/task-scheduler/
package main

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] > h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(item any) {
	*h = append(*h, item.(int))
}
func (h *IntHeap) Pop() any {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type Task struct {
	count, idleTime int
}

// explanation: https://www.youtube.com/watch?v=s8p8ukTyA2I
// max heap tracks task count & use queue to keep task idle until task can be push back to the heap
// T:O(n + nLogN) but since we only have 26 alphabet letters, we can turn nLog(n) into 26 * log(26) which means T:O(1)
// so... the time complexity will be T:O(n), n equals sum of tasks
func leastInterval(tasks []byte, n int) int {
	// T:O(n)
	countMap := make(map[byte]int)
	for _, task := range tasks {
		countMap[task] += 1
	}

	// T:O(26)
	countSlice := []int{}
	for _, cnt := range countMap {
		countSlice = append(countSlice, cnt)
	}

	// T:O(n) for heapify
	maxHeap := IntHeap(countSlice)
	heap.Init(&maxHeap)
	idleQueue := []Task{}

	unitTime := 0
	// ! BE AWARE OF `OR(||)` CONDITION!!!
	// ! ALWAYS CHECK IF SLICE IS EMPTY OR NOT
	for len(maxHeap) > 0 || len(idleQueue) > 0 {
		unitTime += 1

		if len(maxHeap) > 0 {
			cnt := heap.Pop(&maxHeap).(int) - 1
			if cnt > 0 {
				idleQueue = append(idleQueue, Task{count: cnt, idleTime: unitTime + n})
			}
		}

		if len(idleQueue) > 0 && idleQueue[0].idleTime == unitTime {
			queuedTask := idleQueue[0]
			heap.Push(&maxHeap, queuedTask.count)
			idleQueue = idleQueue[1:]
		}
	}

	return unitTime
}
