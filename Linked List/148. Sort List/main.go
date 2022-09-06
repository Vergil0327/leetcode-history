// https://leetcode.com/problems/sort-list/
package main

import "sort"

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func sortListMergeSort(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	left := head
	mid := getMid(head)
	right := mid.Next
	mid.Next = nil // disconnect

	left = sortListMergeSort(left)
	right = sortListMergeSort(right)
	return merge(left, right)
}

func getMid(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow

	// also works!, the difference is is your middle is left-middle or right middle in even list
	// slow, fast := head, head.Next
	// for fast != nil && fast.Next != nil {
	// 	slow = slow.Next
	// 	fast = fast.Next.Next
	// }
	// return slow
}

func merge(left, right *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for left != nil && right != nil {
		if left.Val < right.Val {
			tail.Next = left
			left = left.Next
		} else {
			tail.Next = right
			right = right.Next
		}
		tail = tail.Next
	}

	if left != nil {
		tail.Next = left
	}
	if right != nil {
		tail.Next = right
	}

	return dummy.Next
}

// T:O(nlogn) M:O(n)
func sortList(head *ListNode) *ListNode {
	list := []int{}
	curr := head
	for curr != nil {
		list = append(list, curr.Val)
		curr = curr.Next
	}

	sort.Ints(list)
	curr = head
	i := 0
	for curr != nil {
		curr.Val = list[i]
		curr = curr.Next
		i += 1
	}

	return head
}
