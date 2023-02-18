class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(child)

        highest = -inf
        counter = defaultdict(int)
        def dfs(node, prev):
            nonlocal highest
            if len(children[node]) == 1 and children[node] == prev:
                return 0
            
            size = 0
            scores = []
            for child in children[node]:
                if child == prev: continue
                childSize = dfs(child, node)
                if childSize > 0:
                    scores.append(childSize)
                size += childSize
            parentSubtreeSize = n-1-size
            if parentSubtreeSize > 0:
                scores.append(parentSubtreeSize)

            score = 1
            for subscore in scores:
                score *= subscore
            counter[score] += 1
            highest = max(highest, score)
            
            return size + 1

        dfs(0, -1)
        return counter[highest]
