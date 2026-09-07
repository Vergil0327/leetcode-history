"""
Key Insight & Correct Approach

Step 1 ($t = 0$ Merges):
    Traverse the sorted position array.
    Any contiguous block of robots where position[i+1] - position[i] <= distance merges into one initial group at $t = 0$.
    The initial group takes the speed of its rightmost member.
Step 2 (Catch-up Simulation from Right to Left):
    Scan the reduced groups from right to left while maintaining the speed of the nearest leading group (last_speed).
    If a group behind has speed > last_speed, it will eventually catch up to last_speed and merge into it (so it does not form a new distinct group).
    If a group behind has speed <= last_speed, it will never catch up. Thus, it forms a new distinct group, and its speed becomes the new last_speed for any groups behind it.

---------

When a left group catches a right group, it merges and adopts the right group's position and speed.
This single rule creates a cascade effect that guarantees a simple right-to-left scan is sufficient. Here is why:

1. Cascading Bottlenecks (Transitive Property)
Suppose we have three consecutive groups A, B, and C (from left to right) with speeds v_A, v_B, v_C.
If A catches B (v_A > v_B), A merges into B and now moves at speed v_B.
If B subsequently catches C (v_B > v_C), the combined group (A + B) moves at speed v_C.
Because v_A > v_B > v_C, A would have caught C eventually anyway.
The ultimate speed of any merged chain is always dictated by the rightmost (front) group in that chain.

2. Scanning Right-to-Left Sets the Speed Limit First
When scanning from right to left, we process the group furthest ahead first.
We maintain last_speed as the speed of the frontmost group in the current cluster.
For the next group to the left with speed v_left:
- If v_left > last_speed: This left group moves faster than the front group. It is guaranteed to catch up to the cluster ahead at some point in time. Once it catches up, it adopts last_speed and joins the same group. (No new group formed)
- If v_left <= last_speed: This left group is moving at the same speed or slower than the cluster ahead. The distance between them will either stay constant or increase over time. It can never catch up to the cluster ahead, so it forms a new independent group and sets a new, lower last_speed for anything behind it.

Visual Example
Consider 4 initial groups moving right:
Group: G1  G2  G3  G4
Speed:  5   2   4   1

Scanning Right to Left:
- G4 (Speed 1): Frontmost group. Forms Group 1. last_speed = 1.
- G3 (Speed 4): 4 > 1. G3 catches G4. Merges into G4 (speed becomes 1).
- G2 (Speed 2): 2 > 1. G2 catches the merged (G3 + G4) group. Merges into them.
- G1 (Speed 5): 5 > 1. G1 catches the merged group ahead.

Because every group to the left is faster than 1, all 4 groups eventually collapse into a single group moving at speed 1. We don't need to simulate time or check multi-step chain reactions because the rightmost barrier (speed 1) catches everything behind it!
"""
class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        
        # Step 1: Group robots at t = 0 based on initial positions
        initial_groups_speed = []
        i = 0
        while i < n:
            j = i
            # Merge adjacent robots whose distance is <= distance
            while j + 1 < n and position[j + 1] - position[j] <= distance:
                j += 1
            # The group takes the speed of its rightmost robot (position[j])
            initial_groups_speed.append(speed[j])
            i = j + 1
            
        # Step 2: Scan groups from right to left
        ans = 0
        last_speed = float('inf')
        
        for sp in reversed(initial_groups_speed):
            if sp <= last_speed:
                ans += 1
                last_speed = sp
                
        return ans