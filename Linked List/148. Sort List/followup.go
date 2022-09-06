package main

/*
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Intuition

The Top Down Approach for merge sort uses O(logn) extra space due to recursive call stack. Let's understand how we can implement merge sort using constant extra space using Bottom Up Approach.
The Bottom Up approach for merge sort starts by splitting the problem into the smallest subproblem and iteratively merge the result to solve the original problem.
First, the list is split into sublists of size 1 and merged iteratively in sorted order. The merged list is solved similarly.
The process continues until we sort the entire list.
This approach is solved iteratively and can be implemented using constant extra space. Let's look at the algorithm to implement merge sort in Bottom Up Fashion.

Algorithm

Assume, n is the number of nodes in the linked list.
 - Start with splitting the list into sublists of size 1. Each adjacent pair of sublists of size 1 is merged in sorted order. After the first iteration, we get the sorted lists of size 2. A similar process is repeated for a sublist of size 2. In this way, we iteratively split the list into sublists of size 1,2,4,8 ..1,2,4,8.. and so on until we reach n.
 - To split the list into two sublists of given size beginning from start, we use two pointers, `mid` and `end` that references to the start and end of second linked list respectively. The split process finds the middle of linked lists for the given size.
 - Merge the lists in sorted order as discussed in Approach 1
 - As we iteratively split the list and merge, we have to keep track of the previous merged list using pointer `tail` and the next sublist to be sorted using pointer `nextSubList`.
*/

/*
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None

        def getSize(head):
            counter = 0
            while(head is not None):
                counter +=1
                head = head.next
            return counter

        def split(head, step):
            i = 1
            while (i < step and head):
                head = head.next
                i += 1

            if head is None: return None
            #disconnect
            temp, head.next = head.next, None
            return temp

        def merge(l, r, head):
            cur = head
            while(l and r):
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next

            cur.next = l if l is not None else r
            while cur.next is not None: cur = cur.next
            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        while (bs < size):
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next
*/
// T:O(nlogn) M:O(1)
func sortListMergeSortSpaceOptimized(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	size := getSize(head)
	currSize := 1
	dummy := &ListNode{}
	dummy.Next = head
	var l, r, tail *ListNode = nil, nil, nil

	for currSize < size {
		tail = dummy
		curr := dummy.Next
		for curr != nil {
			l = curr
			r = split(l, currSize)
			curr = split(r, currSize)
			tail = mergeBottomUp(l, r, tail)
		}

		currSize <<= 1 // 1, 2, 4, 8, ...
	}

	return dummy.Next
}

func getSize(head *ListNode) int {
	count := 0
	for head != nil {
		count += 1
		head = head.Next
	}
	return count
}

func split(head *ListNode, step int) *ListNode {
	i := 1
	for head != nil && i < step {
		head = head.Next
		i += 1
	}

	if head == nil {
		return nil
	}

	// disconnect
	var tmp *ListNode = nil
	tmp, head.Next = head.Next, nil
	return tmp
}

func mergeBottomUp(left, right, head *ListNode) *ListNode {
	curr := head
	for left != nil && right != nil {
		if left.Val < right.Val {
			curr.Next, left = left, left.Next
		} else {
			curr.Next, right = right, right.Next
		}
		curr = curr.Next
	}

	if left != nil {
		curr.Next = left
	} else {
		curr.Next = right
	}

	for curr.Next != nil {
		curr = curr.Next
	}

	return curr
}
