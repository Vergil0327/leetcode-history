# Intuition

constraints:
- only 2 extra edges can be added.
- graph can be disconnected.

due to constraints above, the only thing we need to concern is **odd degree edge**

thus, find all the **odd degree edges** first and discuss case by case:

**case 1: more than 4 odd degree nodes**

it's impossible to make them even degrees by adding <= 2 edges
return **False**

**case 2: 0 odd degree nodes**

each node has even degree, and since graph can be disconnected we can leave disconnected graph alone.
return **True**

**case 3: 2 odd degree nodes**

if we can link them together, return **True**.

    also means we need a method to check if they've already had an edge or not.
    thus, build a **adjacency set** for this check.

if they've already linked together, find another independent node to link.

therefore:
- if there exists an independent node for us to link, return **True**
- else **False**

**case 4: 4 odd degree nodes**

only valid if they are able to link pair by pair because we only have 2 extra edges to make them even degree

since just 4 nodes, brute force to find these two pair

# Complexity
- Time complexity:
$$O(edges.length)$$

- Space complexity:
$$O(edges.length)$$

