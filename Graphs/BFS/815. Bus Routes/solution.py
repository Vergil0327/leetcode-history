# shortest path -> think of BFS
# the tricky part is we shouldn't take the visited bus or revisited same stop again -> use hashset to prune duplicate
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop2bus = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop2bus[stop].append(bus)


        queue = deque([source])
        numBus = 0
        busVisited = set()
        stopVisited = set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur in stopVisited: continue
                stopVisited.add(cur)
                if cur == target: return numBus

                for bus in stop2bus[cur]:
                    if bus in busVisited: continue
                    busVisited.add(bus)
                    for nxt in routes[bus]:
                        if nxt in stopVisited: continue
                        queue.append(nxt)
            numBus += 1
        return -1