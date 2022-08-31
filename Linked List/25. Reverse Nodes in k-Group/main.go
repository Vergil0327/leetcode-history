// https://leetcode.com/problems/reverse-nodes-in-k-group/
package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

// explanation: https://www.youtube.com/watch?v=1UOPsfP85V4
func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head

	groupPrev := dummy

	for {
		kth := getKth(groupPrev, k)
		if kth == nil {
			break
		}

		groupNext := kth.Next

		var prev, curr *ListNode = kth.Next, groupPrev.Next
		for curr != groupNext {
			nxt := curr.Next
			curr.Next = prev
			prev = curr
			curr = nxt
		}

		// k: 2
		// groupPrev			kth
		// 	 dummy -> A -> B -> C -> D -> E
		// 	 dummy ->	B -> A -> C -> D -> E
		// 					 kth	curr
		// 					 prev
		tail := groupPrev.Next // now become tail of reversed group
		groupPrev.Next = prev  // prev becomes head of reversed group
		groupPrev = tail
	}

	return dummy.Next
}

func getKth(node *ListNode, k int) *ListNode {
	for node != nil && k > 0 {
		node = node.Next
		k -= 1
	}

	return node
}
