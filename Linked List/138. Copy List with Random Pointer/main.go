// 138. Copy List with Random Pointer
package main

/**
 * Definition for a Node.
 */
type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

// T:O(n) M:O(n)
func copyRandomList(head *Node) *Node {
	m := map[*Node]*Node{}
	currOld := head
	for currOld != nil {
		m[currOld] = &Node{Val: currOld.Val}
		currOld = currOld.Next
	}

	currOld = head
	for currOld != nil {
		m[currOld].Next = m[currOld.Next]
		m[currOld].Random = m[currOld.Random]
		currOld = currOld.Next
	}

	return m[head]
}

// T:O(n) M:O(1)
func copyRandomOpitimized(head *Node) *Node {
	// 1. copy each node side by side
	iter := head
	for iter != nil {
		nxt := iter.Next
		copy := &Node{Val: iter.Val}
		iter.Next = copy
		copy.Next = nxt

		iter = nxt
	}

	// 2. assign random pointer
	iter = head
	for iter != nil {
		// check nil
		if iter.Random != nil {
			iter.Next.Random = iter.Random.Next
		}

		iter = iter.Next.Next
	}

	// 3. restore original linked list & extract new copy linked list
	dummy := &Node{}
	iter = head
	var copy, copyIter *Node = nil, dummy
	for iter != nil {
		nxt := iter.Next.Next

		// new linked list
		copy = iter.Next
		copyIter.Next = copy
		copyIter = copyIter.Next

		// restore original linked list
		iter.Next = nxt

		iter = nxt
	}

	return dummy.Next
}

// Opitimization Solution
// T:O(n) M:O(1)
// https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
// other resource: https://www.youtube.com/watch?v=EHpS2TBfWQg
/*
An intuitive solution is to keep a hash table for each node in the list, via which we just need to iterate the list in 2 rounds respectively to create nodes and assign the values for their random pointers. As a result, the space complexity of this solution is O(N), although with a linear time complexity.

Note: if we do not consider the space reversed for the output, then we could say that the algorithm does not consume any additional memory during the processing, i.e. O(1) space complexity

As an optimised solution, we could reduce the space complexity into constant. The idea is to associate the original node with its copy node in a single linked list. In this way, we don't need extra space to keep track of the new nodes.

The algorithm is composed of the follow three steps which are also 3 iteration rounds.

Iterate the original list and duplicate each node. The duplicate
of each node follows its original immediately.
Iterate the new list and assign the random pointer for each
duplicated node.
Restore the original list and extract the duplicated nodes.
The algorithm is implemented as follows:

public RandomListNode copyRandomList(RandomListNode head) {
  RandomListNode iter = head, next;

  // First round: make copy of each node,
  // and link them together side-by-side in a single list.
  while (iter != null) {
    next = iter.next;

    RandomListNode copy = new RandomListNode(iter.label);
    iter.next = copy;
    copy.next = next;

    iter = next;
  }

  // Second round: assign random pointers for the copy nodes.
  iter = head;
  while (iter != null) {
    if (iter.random != null) {
      iter.next.random = iter.random.next;
    }
    iter = iter.next.next;
  }

  // Third round: restore the original list, and extract the copy list.
  iter = head;
  RandomListNode pseudoHead = new RandomListNode(0);
  RandomListNode copy, copyIter = pseudoHead;

  while (iter != null) {
    next = iter.next.next;

    // extract the copy
    copy = iter.next;
    copyIter.next = copy;
    copyIter = copy;

    // restore the original list
    iter.next = next;

    iter = next;
  }

  return pseudoHead.next;
}
*/
