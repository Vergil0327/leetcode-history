// https://leetcode.com/problems/linked-list-cycle-ii/
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		// ! both slow, fast start at head, we need move pointer first before we check equality
		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			break
		}
	}

	if fast == nil || fast.Next == nil {
		return nil
	}

	slow2 := head
	for slow != nil {
		if slow == slow2 {
			break
		}
		slow = slow.Next
		slow2 = slow2.Next
	}

	return slow
}

func detectCycleBetter(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		// ! both slow, fast start at head, we need move pointer first before we check equality
		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			break
		}
	}

	if fast == nil || fast.Next == nil {
		return nil
	}

	slow2 := head
	for slow != slow2 {
		slow = slow.Next
		slow2 = slow2.Next
	}

	return slow
}
