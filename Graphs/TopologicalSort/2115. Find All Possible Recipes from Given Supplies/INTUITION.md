# Intuition

since we have clear dependency about recipe and ingredienet,
and start-point are all the supplies.

we can think graph and topological sort and see if we can reach what kind of recipe.

> if indegree[recipie] == 0, it means we have all the ingredients it needs