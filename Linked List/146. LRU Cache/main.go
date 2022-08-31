// https://leetcode.com/problems/lru-cache/
package main

type Element struct {
	Key        int
	Value      int
	Prev, Next *Element
	list       *List
}

type List struct {
	len  int
	root *Element
}

func (l *List) Init() *List {
	root := &Element{}
	root.Prev = root
	root.Next = root
	root.list = l

	return &List{len: 0, root: root}
}

func (l *List) MoveToFront(el *Element) {
	el.Prev.Next = el.Next
	el.Next.Prev = el.Prev

	nxt := l.root.Next

	l.root.Next = el
	el.Prev = l.root
	el.Next = nxt
	nxt.Prev = el
}

func (l *List) AddToFront(el *Element) {
	nxt := l.root.Next

	l.root.Next = el
	el.Prev = l.root
	el.Next = nxt
	nxt.Prev = el

	l.len++
}

func (l *List) Back() *Element {
	return l.root.Prev
}

func (l *List) Remove(el *Element) *Element {
	el.Prev.Next = el.Next
	el.Next.Prev = el.Prev
	el.Next = nil
	el.Prev = nil

	l.len--

	return el
}

type LRUCache struct {
	cap   int
	cache map[int]*Element
	list  *List
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		cap:   capacity,
		cache: make(map[int]*Element),
		list:  new(List).Init(),
	}
}

func (this *LRUCache) Get(key int) int {
	if el, ok := this.cache[key]; ok {
		this.list.MoveToFront(el)
		return el.Value
	}

	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if el, ok := this.cache[key]; ok {
		el.Value = value
		this.list.MoveToFront(el)
		return
	}

	newEl := &Element{Value: value, Key: key}
	this.cache[key] = newEl
	this.list.AddToFront(newEl)

	if this.list.len > this.cap {
		el := this.list.Remove(this.list.Back())
		delete(this.cache, el.Key)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
