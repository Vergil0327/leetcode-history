// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
package main

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]
// Input: head = [1], n = 1
// Output: []
// Input: head = [1,2], n = 2
// Output: [2]

// T:O(2n) M:O(n)
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	len := 0
	curr := head
	for curr != nil {
		len += 1
		curr = curr.Next
	}

	curr = head
	i := 0
	for curr != nil {
		if len-n == 0 {
			nxt := head.Next
			head.Next = nil
			head = nxt
			break
		}

		i += 1
		if i == len-n {
			nxt := curr.Next
			curr.Next = curr.Next.Next
			nxt.Next = nil
			break
		}

		curr = curr.Next
	}

	return head
}

func removeNthFromEndBetter(head *ListNode, n int) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head

	var left, right *ListNode = dummy, head
	for right != nil && n > 0 {
		right = right.Next
		n -= 1
	}

	for right != nil {
		left = left.Next
		right = right.Next
	}

	// delete
	left.Next = left.Next.Next

	return dummy.Next
}
