class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.root = Node(-1, -1)
        self.root.prev = self.root.next = self.root
        self.cap = capacity

    def insertToFront(self, node):
        node.next = self.root.next
        node.prev = self.root
        
        node.next.prev = node
        node.prev.next = node

    def moveToFront(self, node):       
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.root.next
        node.prev = self.root
        node.prev.next = node
        node.next.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToFront(node)
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.moveToFront(self.cache[key])
            return
        
        self.cache[key] = Node(key, value)
        self.insertToFront(self.cache[key])
        
        if len(self.cache) > self.cap:
            removed = self.root.prev
            if removed == self.root: return
            
            removed.prev.next = removed.next
            removed.next.prev = removed.prev
            removed.next = removed.prev = None
            del self.cache[removed.key]