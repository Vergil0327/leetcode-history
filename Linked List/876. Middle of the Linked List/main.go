// https://leetcode.com/problems/middle-of-the-linked-list/
package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

// recommended by https://zhuanlan.zhihu.com/p/349940945
func middleNode(head *ListNode) *ListNode {
	slow, fast := head, head

	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	if fast.Next == nil {
		return slow
	}

	return slow.Next
}
