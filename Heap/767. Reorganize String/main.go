// https://leetcode.com/problems/reorganize-string/
package main

import (
	"container/heap"
)

// explanation: https://www.youtube.com/watch?v=2g_b1aYTHeg&ab_channel=NeetCode
// T:O(nlogn) M:O(n)
func reorganizeString(s string) string {
	freq := map[byte]int{}
	for i := range s {
		freq[s[i]] += 1
	}

	h := MaxFreqHeap([]Word{})
	for b, f := range freq {
		h = append(h, Word{b, f})
	}
	heap.Init(&h)

	str := []byte{}
	for h.Len() > 0 {
		w := heap.Pop(&h).(Word)
		if len(str) == 0 || str[len(str)-1] != w.str {
			str = append(str, w.str)
			if w.freq-1 > 0 {
				heap.Push(&h, Word{w.str, w.freq - 1})
			}
		} else {
			// no more letter to use
			if h.Len() == 0 {
				return ""
			}

			w2 := heap.Pop(&h).(Word)
			str = append(str, w2.str)
			if w2.freq-1 > 0 {
				heap.Push(&h, Word{w2.str, w2.freq - 1})
			}
			heap.Push(&h, w)
		}
	}

	return string(str)
}

type Word struct {
	str  byte
	freq int
}
type MaxFreqHeap []Word

func (h MaxFreqHeap) Len() int               { return len(h) }
func (h MaxFreqHeap) Less(i, j int) bool     { return h[i].freq > h[j].freq }
func (h MaxFreqHeap) Swap(i, j int)          { h[i], h[j] = h[j], h[i] }
func (h *MaxFreqHeap) Push(item interface{}) { *h = append(*h, item.(Word)) }
func (h *MaxFreqHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
