class ListNode:
    def __init__(self, key):
        self.key = key
        self.prev = self.next = None

class AllOne:

    def __init__(self):
        self.counter = defaultdict(int)
        self.val2set = defaultdict(set)

        root = ListNode(0)
        root.next = root.prev = root
        self.val2list = {0: root}
        self.list = root

    def insertAfter(self, target, node):
        node.prev = target
        node.next = target.next
        target.next.prev = node
        target.next = node
    
    def insertBefore(self, target, node):
        node.next = target
        node.prev = target.prev
        target.prev.next = node
        target.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def inc(self, key: str) -> None:
        counter, val2set, val2list = self.counter, self.val2set, self.val2list
        
        val = counter[key]

        counter[key] = val + 1

        # 由於count更新，從原本集合內刪除key，但不可從root node的集合也就是頻率為0的集合中刪除
        # 因為頻率為0代表他本來就不存在
        # 然後加入到新的集合中
        if val > 0: val2set[val].remove(key)
        val2set[val+1].add(key)

        # 如果這是個新的Hashset，那我們也要同時插入到我們的Linked List上這樣之後才能找出Min Key, Max Key
        if len(val2set[val+1]) == 1:
            self.insertAfter(val2list[val], ListNode(val+1))
            val2list[val+1] = val2list[val].next

        # 同樣地，如果原本的集合為空，且不為0的集合的話
        # 為了維護Min Key跟Max Key，我們也必須把他從List Node上刪除
        if val > 0 and len(val2set[val]) == 0:
            self.removeNode(val2list[val])

    def dec(self, key: str) -> None:
        counter, val2set, val2list = self.counter, self.val2set, self.val2list
        
        val = counter[key]
        if val == 0: return # 代表不存在，無法dec，可直接返回

        counter[key] = val - 1

        # 概念同 inc 操作，僅差在dec操作中是val-1可能為0
        val2set[val].remove(key)
        if val-1 > 0: val2set[val-1].add(key)

        if val-1 > 0 and len(val2set[val-1]) == 1:
            self.insertBefore(val2list[val], ListNode(val-1))
            val2list[val-1] = val2list[val].prev
        
        if len(val2set[val]) == 0:
            self.removeNode(val2list[val])

    def getMaxKey(self) -> str:
        if self.list.prev.key == 0: return ""

        val2set = self.val2set
        SET = val2set[self.list.prev.key]
        return next(iter(SET))

    def getMinKey(self) -> str:
        if self.list.next.key == 0: return ""

        val2set = self.val2set
        SET = val2set[self.list.next.key]
        return next(iter(SET))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()