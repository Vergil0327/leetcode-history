class ListNode:
    def __init__(self, txt):
        self.s = txt
        self.prev = self.next = None

class TextEditor:
    # # -> ch -> ch -> ... -> $
    def __init__(self):
        self.list = ListNode("#")
        self.cur = ListNode("$")
        
        self.list.next = self.cur
        self.cur.prev = self.list

    def addText(self, text: str) -> None:
        cur = self.cur
        for ch in text:
            inserted = ListNode(ch)
            inserted.prev = cur.prev
            inserted.next = cur

            inserted.prev.next = inserted
            inserted.next.prev = inserted

    def deleteText(self, k: int) -> int:
        deleted = 0
        cur = self.cur.prev
        while k and cur.s != "#":
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            removed = cur
            cur = cur.prev
            removed.prev = removed.next = None

            deleted += 1
            k -= 1

        return deleted

    def cursorLeft(self, k: int) -> str:
        if self.cur.prev.s == "#":
            return ""
        
        # # X X [target] X X $
        target = self.cur
        while k and target.prev.s != "#":
            k -= 1
            target = target.prev
        
        # remove cursor
        self.cur.prev.next = self.cur.next
        if self.cur.next:
            self.cur.next.prev = self.cur.prev
        
        # insert before target
        self.cur.prev = target.prev
        self.cur.next = target
        self.cur.prev.next = self.cur.next.prev = self.cur


        res = ""
        cur = self.cur.prev
        for _ in range(10):
            if cur and cur.s != "#":
                res = cur.s + res
                cur = cur.prev
            else:
                break
        return res

    def cursorRight(self, k: int) -> str:
        if self.cur.next is None:
            res = ""
            cur = self.cur.prev
            for _ in range(10):
                if cur.s != "#":
                    res = cur.s + res
                    cur = cur.prev
                else:
                    break
                
            return res

        # # X X $ X X [T]
        target = self.cur
        while k and target.next:
            k -= 1
            target = target.next

        # remove cursor
        self.cur.prev.next = self.cur.next
        if self.cur.next:
            self.cur.next.prev = self.cur.prev

        # insert after target
        self.cur.prev = target
        self.cur.next = target.next
        self.cur.prev.next = self.cur
        if self.cur.next:
            self.cur.next.prev = self.cur
        
        res = ""
        cur = self.cur.prev
        for _ in range(10):
            if cur.s != "#":
                res = cur.s + res
                cur = cur.prev
            else:
                break
            
        return res


class TextEditor:
    # # -> ch -> ch -> ... -> $
    def __init__(self):
        self.pre = deque()
        self.suf = deque()

    def addText(self, text: str) -> None:
        for ch in text:
            self.pre.append(ch)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while k and self.pre:
            self.pre.pop()
            k -= 1
            deleted += 1

        return deleted

    def cursorLeft(self, k: int) -> str:
        while k and self.pre:
            self.suf.appendleft(self.pre.pop())
            k -= 1

        n = len(self.pre)
        length = min(10, n)
        res = ""
        for i in range(n-length, n):
            res = res + self.pre[i]
        return res

    def cursorRight(self, k: int) -> str:
        while k and self.suf:
            self.pre.append(self.suf.popleft())
            k -= 1

        n = len(self.pre)
        length = min(10, n)
        res = ""
        for i in range(n-length, n):
            res = res + self.pre[i]
        return res