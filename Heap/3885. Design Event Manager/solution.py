import heapq

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.maxHeap = []
        # Store current valid priority for each eventId
        self.active_priorities = {}
        
        for eid, prio in events:
            # Heap stores [-priority, eventId]
            # -priority: makes it a Max-Heap for priority
            # eventId: on tie, smaller eid comes first (natural sort)
            heapq.heappush(self.maxHeap, [-prio, eid])
            self.active_priorities[eid] = prio

    def updatePriority(self, event_id: int, new_priority: int) -> None:
        if event_id in self.active_priorities:
            self.active_priorities[event_id] = new_priority
            # We MUST push the new version into the heap
            heapq.heappush(self.maxHeap, [-new_priority, event_id])

    def pollHighest(self) -> int:
        # Lazy Deletion: Remove stale entries from the top
        while self.maxHeap:
            prio_neg, eid = self.maxHeap[0]
            # If the priority in heap doesn't match current map, it's stale
            if eid not in self.active_priorities or -prio_neg != self.active_priorities[eid]:
                heapq.heappop(self.maxHeap)
            else:
                break
        
        if not self.maxHeap:
            return -1
        
        # Pop the actual highest
        _, result_id = heapq.heappop(self.maxHeap)
        # Remove from active map so it's no longer "active"
        del self.active_priorities[result_id]
        
        return result_id