# Intuition

**Observation**

1   -> covered 1
1,2 -> covered 1,2,3
1,2,3 -> covered 1,2,3,4,5,6

since 1,2,3 can covered 1~6, if we add 4, it means we add 4,(4+1),(4+2),(4+3),(4+4),(4+5),(4+6), which means we can cover to `10`

therefore, we should maintain current max sum

let's start with `covered = 1` to test if we can covered 1

since `nums` array is sorted, we can add one by one from smallest to largest to extend our `covered`

our target is to make `covered >= n` and we **always add minimum num we need** to extend `covered`

if n=6, nums = [1,2,3] -> if we add `5`, we still need `4` to cover [1,6]
thus, we always add minimum num we need