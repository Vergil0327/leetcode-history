// https://leetcode.com/problems/design-browser-history/
package main

/*
https://leetcode.com/problems/design-browser-history/discuss/674486/Two-Stacks-Pretty-code.

	you can also implement by two stack
	one for current, the other for forward

class BrowserHistory {
public:

	    stack<string> history;
	    stack<string> future;

	    BrowserHistory(string homepage) {
	        history.push(homepage);
	        future = stack<string>(); // Init the forward stack.
	    }

	    void visit(string url) {
	        history.push(url);
	        future = stack<string>(); // Reset the forward stack.
	    }

	    string back(int steps) {
	        while(steps > 0 && history.size() > 1) { // Always keep at least one element in the stack.
	            future.push(history.top());
	            history.pop();
	            steps--;
	        }
	        return history.top();
	    }

	    string forward(int steps) {
	        while(steps > 0 && future.size() > 0) {
	            history.push(future.top());
	            future.pop();
	            steps--;
	        }
	        return history.top();
	    }
	};
*/

type Node struct {
	val        string
	prev, next *Node
}

type List struct {
	root *Node
}

type BrowserHistory struct {
	history *List
	current *Node
}

func Constructor(homepage string) BrowserHistory {
	l := &List{root: &Node{val: homepage}}
	l.root.prev = l.root
	l.root.next = l.root

	return BrowserHistory{history: l, current: l.root}
}

// T:O(1)
func (this *BrowserHistory) Visit(url string) {
	node := &Node{val: url}
	node.prev = this.current
	node.next = this.history.root // clear forward history
	node.prev.next = node
	node.next.prev = node

	this.current = node
}

// T:O(n)
func (this *BrowserHistory) Back(steps int) string {
	for steps > 0 && this.current != this.history.root {
		this.current = this.current.prev
		steps -= 1
	}
	return this.current.val
}

// T:O(n)
func (this *BrowserHistory) Forward(steps int) string {
	for steps > 0 && this.current.next != this.history.root {
		this.current = this.current.next
		steps -= 1
	}
	return this.current.val
}

/**
* Your BrowserHistory object will be instantiated and called as such:
* obj := Constructor(homepage);
* obj.Visit(url);
* param_2 := obj.Back(steps);
* param_3 := obj.Forward(steps);
 */
