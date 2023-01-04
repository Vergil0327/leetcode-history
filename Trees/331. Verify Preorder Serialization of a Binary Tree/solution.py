class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = deque(preorder.split(","))

        root = preorder.popleft()
        children_need = 2 if root != "#" else 0
        if children_need == 0 and preorder: return False

        while preorder:
            node = preorder.popleft()
            children_need -= 1
            if node != "#":
                children_need += 2
            if children_need == 0 and preorder: return False

        return children_need == 0
