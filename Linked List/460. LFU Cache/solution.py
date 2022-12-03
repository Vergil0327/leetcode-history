class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.key2val = {}
        self.key2freq = defaultdict(lambda: 1)
        def initRoot():
            root = ListNode(-1, -1)
            root.next = root.prev = root
            return root
        self.freq2keys = defaultdict(initRoot)
        self.min = 1
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        self.key2freq[key] += 1
        self.disconnect(self.key2val[key])
        root = self.freq2keys[self.key2freq[key]]
        self.insertToFront(root, self.key2val[key])
        
        if self.freq2keys[self.min] == self.freq2keys[self.min].next == self.freq2keys[self.min].prev:
            self.min += 1
        
        return self.key2val[key].val
        

    def insertToFront(self, root, node):
        node.next = root.next
        node.prev = root
        
        node.next.prev = node
        node.prev.next = node
        
    def disconnect(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        
    def put(self, key: int, val: int) -> None:
        if self.cap <= 0: return
        
        if key in self.key2val:
            # udpate val
            node = self.key2val[key]
            node.val = val
            
            # disconnect
            self.disconnect(node)
            
            # increment freq
            self.key2freq[key] += 1
            freq = self.key2freq[key]

            # move node to new freq
            self.insertToFront(self.freq2keys[freq], node)
            
            # check validity of self.min
            if self.freq2keys[self.min] == self.freq2keys[self.min].next == self.freq2keys[self.min].prev:
                self.min += 1
            return
        
        # check capacity
        if len(self.key2val) == self.cap:
            root = self.freq2keys[self.min]
            removed = root.prev
            if removed.key != -1:
                self.disconnect(removed)
                del self.key2val[removed.key]
                del self.key2freq[removed.key]


        # insert value & freq
        node = ListNode(key, val)
        self.key2val[key] = node
        self.key2freq[key] = 1
        
        # insert node to freq
        self.insertToFront(self.freq2keys[1], node)
        
        # don't forget to point `min` to current least frequncy
        self.min = 1
