class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        nodes = {x for word in words for x in word}
        for length in range(len(nodes) + 1):
            valid_doubles = []
            for doubles in combinations(nodes, length):
                graph = defaultdict(list)
                for word in words:
                    u, v = word[0], word[1]
                    if u not in doubles and v not in doubles:
                        graph[u].append(v)
                if not has_cycle(graph):
                    valid_doubles.append(doubles)
            if valid_doubles: break
                
        res = []
        for doubles in valid_doubles:
            row = [0] * 26
            for x in nodes:
                row[ord(x)-ord("a")] = 1
            for y in doubles:
                row[ord(y)-ord("a")] = 2
            res.append(row)
        return res


NEW, VISITING, DONE = range(3)
def has_cycle(graph):
    color = defaultdict(int)
    def dfs(node):
        if color[node] != NEW:
            return color[node] == VISITING
        color[node] = VISITING
        if any(dfs(nei) for nei in graph[node]):
            return True
        color[node] = DONE
        return False

    return any(dfs(node) for node in list(graph.keys()))
