class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # map boundary points (x,y) to 4 axis
        axis = [[], [], [], []] # Left, Top, Right, Bottom
        for x, y in points:
            if x == 0 and y != 0:
                axis[0].append((x,y))
            elif x != 0 and y == side:
                axis[1].append((x,y))
            elif x == side and y != side:
                axis[2].append((x,y))
            else:
                axis[3].append((x,y))
        
        # Sort points in each line (Right and Bottom lines are
        # sorted in reverse to sort all points in clockwise dir)
        axis[0].sort()
        axis[1].sort()
        axis[2].sort(reverse=True)
        axis[3].sort(reverse=True)
        extended_axis = [*axis[0],*axis[1],*axis[2],*axis[3]] # Recombine points

        def check(d):
            queue = deque([(extended_axis[0][0], extended_axis[0][1], extended_axis[0][0], extended_axis[0][1], 1)]) # Start processing from point 0
            count = 1

            for i in range(1, len(extended_axis)):
                x, y = extended_axis[i]
                endx, endy = x, y # Coordinates of path endpoint
                cur_len = 1 # Current path length

                while len(queue): # Try to pop points from the front of the deque (greedily judge far-most path endpoint from current (x,y) point)
                    xi, yi, pathx, pathy, length = queue[0]
                    if abs(x-xi) + abs(y-yi) >= d: # Current point is at a distance d from the point at the deque head
                        if length+1 >= cur_len and abs(x-pathx) + abs(y-pathy) >= d:
                            # If including the current point is an improvement in length AND
                            # If it is the last point, it is at a distance d from the start of the path
                            # update values -> append current point to queue[0]
                            cur_len = length + 1
                            endx, endy = pathx, pathy
                            count = max(count, cur_len)
                        queue.popleft() # Always pop the deque head because we found the closest point at a distance d
                    else:
                        break # No more points can be popped

                queue.append((x, y, endx, endy, cur_len)) # Add current point with path details to deque
            return count >= k
            

        l, r = 0, 2 * side
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l
