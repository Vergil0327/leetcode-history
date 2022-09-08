// https://leetcode.com/problems/odd-even-linked-list/

package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenListConcise(head *ListNode) *ListNode {
	// edge case
	if head == nil {
		return nil
	}

	evenHead := head.Next

	// 1,2,3,4,5,6,7
	// o e
	//     o e
	//         o e
	//             o e
	odd, even := head, head.Next
	for even != nil && even.Next != nil {
		odd.Next = even.Next
		odd = odd.Next
		even.Next = odd.Next
		even = even.Next
	}
	odd.Next = evenHead

	return head
}

func oddEvenList(head *ListNode) *ListNode {
	// edge: []
	if head == nil {
		return nil
	}

	// edge: [1]
	if head.Next == nil {
		return head
	}

	dummy := &ListNode{Next: head.Next}

	prev := head
	curr := head.Next
	count := 0
	for curr.Next != nil {
		prev.Next = curr.Next
		prev, curr = curr, curr.Next
		count += 1
	}

	if count%2 == 0 {
		prev.Next = dummy.Next
		return head
	}

	curr.Next = dummy.Next
	prev.Next = nil
	return head
}
