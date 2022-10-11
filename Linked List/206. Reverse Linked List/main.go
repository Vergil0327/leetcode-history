package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time: O(n),  Memory: O(1)
func reverseList(head *ListNode) *ListNode {
	// cursor
	var prev, curr *ListNode = nil, head

	for curr != nil {
		tmpNext := curr.Next
		curr.Next = prev
		prev = curr
		curr = tmpNext
	}
	return prev
}

// T: O(n), M(n)
func reverseListRecursive(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	newHead := head
	if head.Next != nil {
		newHead = reverseListRecursive(head.Next)
		head.Next.Next = head
	}
	head.Next = nil
	return newHead
}
