// https://leetcode.com/problems/top-k-frequent-words/
package main

import "container/heap"

/* Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space? */
// use MinHeap to pop out lower frequency & string in larger lexicographical order
func topKFrequentFollowUp(words []string, k int) []string {
	freq := map[string]int{}
	for _, word := range words {
		freq[word] += 1
	}

	h := MinHeap([]Word{})

	for word, f := range freq {
		heap.Push(&h, Word{str: word, freq: f})
		if h.Len() > k {
			heap.Pop(&h)
		}
	}

	res := make([]string, h.Len())
	for i := len(res) - 1; i >= 0; i-- {
		res[i] = heap.Pop(&h).(Word).str
	}
	return res
}

// klogn
func topKFrequent(words []string, k int) []string {
	freq := map[string]int{}
	for _, word := range words {
		freq[word] += 1
	}

	h := MaxHeap([]Word{})
	for word, f := range freq {
		h = append(h, Word{str: word, freq: f})
	}
	heap.Init(&h)

	res := []string{}
	for k > 0 {
		res = append(res, heap.Pop(&h).(Word).str)
		k -= 1
	}

	return res
}

type Word struct {
	freq int
	str  string
}

type MaxHeap []Word

func (h MaxHeap) Len() int {
	return len(h)
}
func (h MaxHeap) Less(i, j int) bool {
	// compare string lexicographically
	if h[i].freq == h[j].freq {
		return h[i].str < h[j].str
	}

	return h[i].freq > h[j].freq
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MaxHeap) Push(item interface{}) {
	*h = append(*h, item.(Word))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type MinHeap []Word

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	if h[i].freq == h[j].freq {
		// compare string reverse lexicographically
		return h[i].str > h[j].str
	}

	return h[i].freq < h[j].freq
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(Word))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
