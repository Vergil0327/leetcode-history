// https://leetcode.com/problems/merge-k-sorted-lists/

package main

import "container/heap"

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

// Divide&Conquer
// T:O(nLogk), merge takes O(n)
// M: O(n) or O(1)
func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}

	// T:O(n)
	var merge func(left, right *ListNode) *ListNode = func(left, right *ListNode) *ListNode {
		dummy := &ListNode{}
		curr := dummy
		for left != nil && right != nil {
			if left.Val < right.Val {
				curr.Next = left
				left = left.Next
			} else {
				curr.Next = right
				right = right.Next
			}
			curr = curr.Next
		}

		if left != nil {
			curr.Next = left
		} else {
			curr.Next = right
		}

		return dummy.Next
	}

	/* // M:O(n)
	for len(lists) > 1 {
		mergedList := []*ListNode{}
		for i := 0; i < len(lists); i += 2 {
			left := lists[i]
			var right *ListNode
			if i+1 < len(lists) {
				right = lists[i+1]
			}
			mergedList = append(mergedList, merge(left, right))
		}
		lists = mergedList
	}

	return lists[0] */

	// M:O(1) in-place
	N := len(lists)
	interval := 1
	for interval < N {
		for i := 0; i < N-interval; i += interval * 2 {
			lists[i] = merge(lists[i], lists[i+interval])
		}
		interval *= 2
	}

	return lists[0]
}

// T:O(nlogk), k is length of lists
func mergeKListsHeap2(lists []*ListNode) *ListNode {
	h := MinHeap([]*ListNode{})
	for _, list := range lists {
		if list != nil {
			heap.Push(&h, list)
		}
	}

	dummy := &ListNode{}
	curr := dummy
	for h.Len() > 0 {
		node := heap.Pop(&h).(*ListNode)
		curr.Next = node
		curr = curr.Next
		if node.Next != nil {
			heap.Push(&h, node.Next)
		}
	}

	return dummy.Next
}

// T:O(nlogn), n for total amount of *ListNode
func mergeKListsHeap1(lists []*ListNode) *ListNode {
	h := MinHeap([]*ListNode{})
	for _, list := range lists {
		for list != nil {
			heap.Push(&h, list)
			list, list.Next = list.Next, nil // disconnect
		}
	}

	dummy := &ListNode{}
	curr := dummy
	for h.Len() > 0 {
		curr.Next = heap.Pop(&h).(*ListNode)
		curr = curr.Next
	}

	return dummy.Next
}

type MinHeap []*ListNode

func (h MinHeap) Len() int {
	return len(h)
}
func (h MinHeap) Less(i, j int) bool {
	return h[i].Val < h[j].Val
}
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *MinHeap) Push(item interface{}) {
	*h = append(*h, item.(*ListNode))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}
