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

// T: O(n), M: O(n)
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	m := map[ListNode]interface{}{}

	for head.Next != nil {
		if _, ok := m[*head]; ok {
			return true
		}

		m[*head] = struct{}{}

		next := head.Next
		head = next
	}

	return false
}

// T: O(n), M: O(1)
// if it's a cycle, fast pointer will get closer by 1 further node each iteration
// https://www.youtube.com/watch?v=gBTe7lFR3vc
func hasCycleBetter(head *ListNode) bool {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}

	return false
}
