class ListNode:
    __slots__ = "val", "next", "down"
    def __init__(self, num=-1, next=None, down=None):
        self.val = num
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = ListNode() # dummy head

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            # Move to the right in the current level
            while node.next and node.next.val < target:
                node = node.next
            if node.next and node.next.val == target:
                return True
            # Move to the the next level
            node = node.down
        return False

    def add(self, num: int) -> None:
        nodes = []
        cur = self.head
        while cur:
            while cur.next and cur.next.val < num:
                cur = cur.next
            nodes.append(cur)
            cur = cur.down
        
        should_insert = True
        down = None
        while should_insert and nodes:
            node = nodes.pop()
            node.next = ListNode(num, node.next, down)
            down = node.next
            should_insert = (random.getrandbits(1) == 0) # coin flip, 判斷下一層還該不該插入該節點

        if should_insert:
            self.head = ListNode(-1, None, self.head)
        
    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            # Move to the next node in the current level
            while node.next and node.next.val < num:
                node = node.next
            # Find the target node and delete
            if node.next and node.next.val == num:
                node.next = node.next.next
                found = True
            # Move to the next level
            node = node.down      
        return found
