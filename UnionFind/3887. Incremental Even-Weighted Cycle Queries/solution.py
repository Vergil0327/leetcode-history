class Solution:
    def numberOfEdgesAdded(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        # parity[i] is the parity of the path weight from node i to parent[i]
        parity = [0] * n
        # rank[i] is the height of the tree rooted at i
        rank = [1] * n
        
        def find(i):
            if parent[i] == i:
                return i, 0
            
            # Recursive Path Compression
            root, root_dist = find(parent[i])
            parent[i] = root
            # Update current node's distance to be relative to the new root
            parity[i] = (parity[i] + root_dist) % 2
            return parent[i], parity[i]

        added_count = 0
        
        for u, v, w in edges:
            root_u, d_u = find(u)
            root_v, d_v = find(v)
            
            if root_u != root_v:
                # Union by Rank
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v # root_v is new root
                    parity[root_u] = (d_u + d_v + w) % 2 # update parity of root_u to new root
                    rank[root_v] += rank[root_u]
                else:
                    # u becomes the new parent (handles > and == cases)
                    parent[root_v] = root_u
                    parity[root_v] = (d_u + d_v + w) % 2
                    rank[root_u] += rank[root_v]
                
                added_count += 1
            else:
                # Cycle check: existing path (u->root->v) must match edge weight w
                if (d_u + d_v) % 2 == w:
                    added_count += 1
                    
        return added_count