// SUBSCRIBE TO UNLOCK: https://leetcode.com/problems/first-unique-number/
package main

/*
Example 1:
Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:
Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]
Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:
Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]
Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
*/

type FirstUnique struct {
	exist map[int]int
	queue []int
}

// T:O(n)
func New(nums []int) FirstUnique {
	exist := make(map[int]int)
	q := []int{}

	for _, num := range nums {
		exist[num] += 1
	}

	for _, num := range nums {
		if cnt := exist[num]; cnt == 1 {
			q = append(q, num)
		}
	}
	return FirstUnique{exist: exist, queue: q}
}

func (uniq *FirstUnique) Add(num int) {
	uniq.exist[num] += 1
	if uniq.exist[num] == 1 {
		uniq.queue = append(uniq.queue, num)
	} else {
		for len(uniq.queue) > 0 && uniq.exist[uniq.queue[0]] > 1 {
			uniq.queue = uniq.queue[1:]
		}
	}
}

func (uniq *FirstUnique) ShowFirstUnique() int {
	if len(uniq.queue) > 0 {
		return uniq.queue[0]
	}

	return -1
}
