# Intuition

find starting point, then BFS?
- record current posisiton
- record keys we have
  - since key <= 6 => we can use 6 bits to store
- keep BFS
- since node might visite multiple times, our visited set should store their position with their state

we should prune duplication by their state, not just position.

if we visited (i, j) with 0 key, we can visit (i, j) again with 1 key or more becuase we might be able to open lock or turn back.

thus, our visited set should store (i, j, keyState)

then our BFS should cost:

O(m * n * keyState) = O(30 * 30 * (1<<6)) => it can work

so, we can do BFS to explore

- if we hit wall or boundary, skip
- if we hit lock and we don't have key, skip
- if we visit next position with same keyState, skip
- if we hit key, we pick it and update keyState


the key point is what is the exact duplication state we should prune.

not just skip if we reach same old position, what we really care about is when we reach (i, j) position if we still have same key state