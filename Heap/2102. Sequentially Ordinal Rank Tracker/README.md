[2102. Sequentially Ordinal Rank Tracker](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/)

`Hard`

A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

Adding scenic locations, one at a time.
Querying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).
For example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.
Note that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.

Implement the SORTracker class:

SORTracker() Initializes the tracker system.
void add(string name, int score) Adds a scenic location with name and score to the system.
string get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).
 
```
Example 1:

Input
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
Output
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation
SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get();              // The sorted locations, from best to worst, are: branford, bradford.
                            // Note that branford precedes bradford due to its higher score (3 > 2).
                            // This is the 1st time get() is called, so return the best location: "branford".
tracker.add("alps", 2);     // Add location with name="alps" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford.
                            // Note that alps precedes bradford even though they have the same score (2).
                            // This is because "alps" is lexicographically smaller than "bradford".
                            // Return the 2nd best location "alps", as it is the 2nd time get() is called.
tracker.add("orland", 2);   // Add location with name="orland" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford, orland.
                            // Return "bradford", as it is the 3rd time get() is called.
tracker.add("orlando", 3);  // Add location with name="orlando" and score=3 to the system.
tracker.get();              // Sorted locations: branford, orlando, alps, bradford, orland.
                            // Return "bradford".
tracker.add("alpine", 2);   // Add location with name="alpine" and score=2 to the system.
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "bradford".
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "orland".
```

Constraints:

- name consists of lowercase English letters, and is unique among all locations.
- 1 <= name.length <= 10
- 1 <= score <= 10^5
- At any time, the number of calls to get does not exceed the number of calls to add.
- At most 4 * 10^4 calls in total will be made to add and get.

Accepted
13.5K
Submissions
20.8K
Acceptance Rate
65.0%

<details>
<summary>Hint 1</summary>

If the problem were to find the median of a stream of scenery locations while they are being added, can you solve it?

</details>
<details>
<summary>Hint 2</summary>

We can use a similar approach as an optimization to avoid repeated sorting.

</details>
<details>
<summary>Hint 3</summary>

Employ two heaps: left heap and right heap. The left heap is a max-heap, and the right heap is a min-heap. The size of the left heap is k + 1 (best locations), where k is the number of times the get method was invoked. The other locations are maintained in the right heap.

</details>
<details>
<summary>Hint 4</summary>

Every time when add is being called, we add it to the left heap. If the size of the left heap exceeds k + 1, we move the head element to the right heap.

</details>
<details>
<summary>Hint 5</summary>

When the get method is invoked again (the k + 1 time it is invoked), we can return the head element of the left heap. But before returning it, if the right heap is not empty, we maintain the left heap to have the best k + 2 items by moving the best location from the right heap to the left heap.

</details>
