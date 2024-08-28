class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = Counter()
        for i in range(len(recipes)):
            indeg[recipes[i]] = 0

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
                indeg[recipes[i]] += 1

        queue = deque(supplies)
        res = []
        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                for nxt in graph[item]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        res.append(nxt)
                        queue.append(nxt)
        return res