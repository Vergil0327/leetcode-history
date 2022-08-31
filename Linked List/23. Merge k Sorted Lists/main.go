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

/*
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[

	1->4->5,
	1->3->4,
	2->6

]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
*/

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

// T:O(Nlogk)
func mergeKListsHeap(lists []*ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy
	h := MinHeap([]*ListNode{})
	heap.Init(&h)

	for _, list := range lists {
		if list != nil {
			heap.Push(&h, list)
		}
	}

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

// Neetcode explanation: https://www.youtube.com/watch?v=q5a5OiGbT6Q
// T:O(nLogK) M:O(n) for new linked list
func mergeKListsDivideConquer(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}

	var merge = func(left, right *ListNode) *ListNode {
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

	return lists[0]
}

// Approach 5: Merge with Divide And Conquer
// https://leetcode.com/problems/merge-k-sorted-lists/solution/
// Time complexity : O(Nlogk) where k is the number of linked lists.
// We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
// Sum up the merge process and we can get: O(∑[i=1 to log2(k)](N)=O(Nlogk)
// Space complexity : O(1)
// We can merge two sorted linked lists in O(1) space.
func mergeKListsDivideConquerInPlace(lists []*ListNode) *ListNode {
	var merge = func(left, right *ListNode) *ListNode {
		dummy := &ListNode{}
		curr := dummy
		for left != nil && right != nil {
			if left.Val <= right.Val {
				curr.Next = left
				left = left.Next
			} else {
				curr.Next = right
				right = right.Next
			}
			curr = curr.Next
			curr.Next = nil
		}
		if left != nil {
			curr.Next = left
		} else {
			curr.Next = right
		}

		return dummy.Next
	}

	// ? Clever way to merge in place
	N := len(lists)
	interval := 1
	for interval < N {
		for i := 0; i < N-interval; i += interval * 2 {
			lists[i] = merge(lists[i], lists[i+interval])
		}
		interval *= 2
	}

	if N > 0 {
		return lists[0]
	}
	return nil
}

// just passed
// Runtime: 8 ms, faster than 92.58% of Go online submissions for Merge k Sorted Lists.
// Memory Usage: 5.8 MB, less than 49.74% of Go online submissions for Merge k Sorted Lists.
func mergeKListsJustPassed(lists []*ListNode) *ListNode {
	var merge = func(left, right []*ListNode) []*ListNode {
		leftNode := left[0]
		rightNode := right[0]
		dummy := &ListNode{}
		curr := dummy
		for leftNode != nil && rightNode != nil {
			if leftNode.Val < rightNode.Val {
				tmp := leftNode.Next
				curr.Next = leftNode
				curr.Next.Next = nil
				leftNode = tmp
			} else {
				tmp := rightNode.Next
				curr.Next = rightNode
				curr.Next.Next = nil
				rightNode = tmp
			}
			if curr.Next != nil {
				curr = curr.Next
			}
		}

		if leftNode != nil {
			curr.Next = leftNode
		}
		if rightNode != nil {
			curr.Next = rightNode
		}

		return []*ListNode{dummy.Next}
	}

	var partition func(lists []*ListNode) []*ListNode
	partition = func(lists []*ListNode) []*ListNode {
		if len(lists) <= 1 {
			return lists
		}
		mid := len(lists) / 2

		left := partition(lists[:mid])
		right := partition(lists[mid:])
		return merge(partition(left), partition(right))
	}

	N := len(lists)
	tmp := []*ListNode{}
	for i := 0; i < N; i = i + 2 {
		if i+2 > N {
			tmp = append(tmp, partition(lists[i:])...)
			break
		}
		tmp = append(tmp, partition(lists[i:i+2])...)
	}

	ans := partition(tmp)
	if len(ans) > 0 {
		return ans[0]
	} else {
		return nil
	}
}

// OUT OF MEMORY, too many callstacks
func mergeKListsTIMEOUT(lists []*ListNode) *ListNode {
	var merge = func(left, right []*ListNode) []*ListNode {
		leftNode := left[0]
		rightNode := right[0]
		dummy := &ListNode{}
		curr := dummy
		for leftNode != nil && rightNode != nil {
			if leftNode.Val < rightNode.Val {
				tmp := leftNode.Next
				curr.Next = leftNode
				curr.Next.Next = nil
				leftNode = tmp
			} else {
				tmp := rightNode.Next
				curr.Next = rightNode
				curr.Next.Next = nil
				rightNode = tmp
			}
			if curr.Next != nil {
				curr = curr.Next
			}
		}

		if leftNode != nil {
			curr.Next = leftNode
		}
		if rightNode != nil {
			curr.Next = rightNode
		}

		return []*ListNode{dummy.Next}
	}

	var partition func(lists []*ListNode) []*ListNode
	partition = func(lists []*ListNode) []*ListNode {
		if len(lists) <= 1 {
			return lists
		}
		mid := len(lists) / 2

		left := partition(lists[:mid])
		right := partition(lists[mid:])
		return merge(partition(left), partition(right))
	}

	return partition(lists)[0]
}
