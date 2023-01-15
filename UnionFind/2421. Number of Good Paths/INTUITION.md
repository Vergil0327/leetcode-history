# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
come up with Union-Find solution but the tricky part is the order of union step...

hard to explain my thought clearly but I try my best.

first, since all nodes between starting node and ending node should be **less than or equal to** starting node (= ending node) for good path, it's convenient for us to start to union node together from smallest value to largest value.

- if we start from largest value, we need to iteratively check if good path with lower value two-end node exists in current union grups.

- but if we start from lowest to largest node, we just count number of good path step by step

thus, we can sort the edges with value[node] in increasing order
```
edges.sort(key=lambda x:(vals[x[1]]))
```

the most difficult condition to come up with is we need to choose node with **larger** value for sorting edges in increasing order, that's the reason why I sort each edge with node value. (I need to know which node in edge has larger value)

the reason why I do this is when I try to union two groups together and count good path, I realize that the smaller one can't form the good path or it've already been taken into consideration in previous step.

# Approach
<!-- Describe your approach to solving the problem. -->

- start from edge with lowest node value to largest
- union group with smaller representative into group with larger representative and only update `counter` of larger value group.
    - node lower value is useless in future

the way to count good path in each union step is:

```
for edge in edges
    edge = [u, v] and v with larger value
    good path += (# of vals[v] in gruopA) * (# of vals[v] in groupB)

node u can't form any good path in this turn
```

Example
```
vals  = [5,1,4,2,1,5,4,3]
edges = [[1,0],[2,0],[3,2],[4,2],[5,4],[6,4],[6,7]]

and we want to union group A with group B by connecting edge [2,5] currently

good path = # of vals[5] in gruopA * # of vals[5] in groupB

group A:
7(3)-6(4)-4(1)-2(4)-3(2)
     |          
     5(5)
     
group B:        
           1(1)-0(5)

into

7(3)-6(4)-4(1)-2(4)-3(2)
     |          |
     5(5)       |
           1(1)-0(5)

one new good path is 5-6-4-2-0
```

# Complexity
- Time complexity:
$$O(nlogn)$$ for edges sorting

- Space complexity:
$$O(n)$$ for union-find

