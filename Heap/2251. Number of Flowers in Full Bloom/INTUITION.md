# Intuition

use diff array to denote full-bloom of each flower
then we just iterate people to check how many kind of full-bloom flower they can see
but starti <= endi <= $10^9$, it's too large for us to build difference array

so, maybe we can use two pointers?
iterate people[i] chronologically and add sorted(flowers)[j] when `sorted(flowers)[j][0] <= people[i]` and remove when `sorted(flowers)[j][1] < people[i]`

then, res[i] should be how many flowers still exist

thus, we use two pointers to iterate people and flowers

- first, we sort people and flowers by start_time
  - remember to store original index of people after sorting. we need it to udpate res[i]
- use **min heap** to store flowers[j][1]
- when flowers[j][0] <= people[i], we add flowers[j][1]
- when flowers in **min heap** no more full bloom which means minHeap[0] < people[i], we pop it out
- then, res[i] = len(minHeap) when we iterate i from 0 to len(people)-1