class LockingTree:

    def __init__(self, parent: List[int]):
        n = self.n = len(parent)

        self.parent = defaultdict(lambda: -1)
        self.leaves = defaultdict(list)
        for i in range(n):
            self.parent[i] = parent[i]
            if parent[i] != -1:
                self.leaves[parent[i]].append(i)

        self.vault = defaultdict(lambda: {"lock": False, "lockBy": -1})
        
    def lock(self, num: int, user: int) -> bool:
        vault = self.vault

        if vault[num]["lock"]: return False

        vault[num]["lock"] = True
        vault[num]["lockBy"] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        vault = self.vault

        if not vault[num]["lock"] or vault[num]["lockBy"] != user: return False

        vault[num]["lock"] = False
        vault[num]["lockBy"] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        vault = self.vault

        if vault[num]["lock"]: return False

        # check ancestor
        parent = self.parent
        curr = num
        while parent[curr] != -1:
            if vault[parent[curr]]["lock"]: return False
            curr = parent[curr]

        # check descendants by BFS
        leaves = self.leaves
        queue = deque(leaves[num])
        cnt = 0
        tmp = vault.copy()
        while queue:
            for _ in range(len(queue)):
                leaf = queue.popleft()

                if vault[leaf]["lock"]:
                    cnt += 1
                    tmp[leaf]["lock"] = False
                    tmp[leaf]["lockBy"] = -1

                for nei in leaves[leaf]:
                    queue.append(nei)
        if cnt == 0: return False

        tmp[num]["lock"] = True
        tmp[num]["lockBy"] = user
        self.vault = tmp
        return True