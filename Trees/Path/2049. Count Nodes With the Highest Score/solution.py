class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)

        nxt = defaultdict(list)
        for node, parent in enumerate(parents):
            if parent != -1:
                nxt[parent].append(node)

        counter = defaultdict(int)
        highest = -inf

        # iterate through bi-directional graph
        def dfs(node, prev):
            nonlocal highest

            size = 1
            scores = []
            for child in nxt[node]:
                if child == prev: continue
                subtree_size = dfs(child, node)
                scores.append(subtree_size)
                size += subtree_size

            # parent_subtree_size
            if n-size > 0:
                scores.append(n-size)

            score = 1
            for sc in scores:
                score *= sc
            counter[score] += 1
            highest = max(highest, score)

            return size

        dfs(0, -1)
        return counter[highest]