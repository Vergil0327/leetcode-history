# Intuition


There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
transfrom nums[i] into set of factors and union their factors together, because node's factor is the key and node itself is the bridge to connect each factor's groups together.

see example1.

4 = 2*2
6 = 2*3 => connect group-2 and group-3
15 = 3*5 => connect group-3 and group-5
35 = 5*7 => connect group-5 and group-7
thus if x = a*b*c*d*e => x connect group-a, group-b, group-c, group-d, group-e together

thus, turn nums[i] into a*b*c*d...
then union factors: union(a, b), union(a, c), union(a, d), ...
after all, connected component size += 1 (nums[i] itself) => rank[find(a)] += 1

the final answer should be max(rank)

# Complexity

- time complexity

$$O(n * sqrt(n))**

- space complexity

$$O(max(nums[i]))$$