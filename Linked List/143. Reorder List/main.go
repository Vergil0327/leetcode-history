// https://leetcode.com/problems/reorder-list/
package main

//  Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Input: head = [1,2,3,4]
// Output: [1,4,2,3]

// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

// T:O(n) M:O(n)
func reorderList(head *ListNode) {
	list := []*ListNode{}
	curr := head
	for curr.Next != nil {
		list = append(list, curr)
		curr = curr.Next
	}
	list = append(list, curr)

	for i, j := 0, len(list)-1; i < j; i, j = i+1, j-1 {
		list[i].Next = list[j]
		list[j].Next = list[i+1]

		if len(list)%2 == 0 && i == j-1 {
			list[j].Next = nil
		} else if len(list)%2 != 0 && j == len(list)/2+1 {
			list[j].Next.Next = nil
		}
	}
}

// Explanation: https://www.youtube.com/watch?v=S5bfdUTrKLM
// T: O(n), M: O(1)
func reorderListBetter(head *ListNode) {
	// FIND MIDDLE
	// for EVEN number like head = [1,2,3,4]
	// slow point to 2, end of left-half and fast point to the end of linked list
	// for ODD number like head = [1,2,3,4,5]
	// slow point to 3, end of left-half and fast point to the next of end of linked list (nil value)
	// both condition will be fine for us to merge
	slow, fast := head, head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// reverse second half
	var prev, second *ListNode = nil, slow.Next
	slow.Next = nil //  break pointer between first & second half
	for second != nil {
		nxt := second.Next
		second.Next = prev
		prev = second
		second = nxt
	}

	// merge
	second = prev // prev will be second-half's new head after reverse
	for second != nil {
		tmp1, tmp2 := head.Next, second.Next
		head.Next = second
		second.Next = tmp1
		head, second = tmp1, tmp2
	}
}

func genLinkedList(list []int) *ListNode {
	dummy := &ListNode{Val: 0}
	var curr *ListNode = dummy
	for _, v := range list {
		tmp := &ListNode{Val: v}
		curr.Next = tmp
		curr = curr.Next
	}
	return dummy.Next
}
