class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        visited = set(rooms[0]+[0])
        while queue:
            for _ in range(len(queue)):
                key = queue.popleft()
                for room in rooms[key]:
                    if room not in visited:
                        visited.add(room)
                        queue.append(room)

        return len(visited) == len(rooms)
