package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	slow, fast := head, head
	for fast != nil {
		if slow.Val != fast.Val {
			slow.Next = nil
			slow.Next = fast
			slow = slow.Next
		}

		fast = fast.Next
	}

	// remove duplicate
	slow.Next = nil

	return head
}
