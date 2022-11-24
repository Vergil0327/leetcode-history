if n=1: [1], only one possible result

if n=2: [1,2]
  1. 1 as root, 2 as right node
  2. 2 as root, 1 as right node

if n=3: [1,2,3]
  1. 1 as root
     - [2, 3] has `numTrees(2)` possible combinations as right subtree
     - [] as `numTrees(0)` possible combinations as left subtree
     - total = `numTrees(0)` * `numTrees(2)`. kind of like factorial(0) * factorial(2)
  2. 2 as root
     - [1] has `numTrees(1)` possible combinations as left subtree
     - [3] has `numTrees(1)` possible combinations as right subtree
     - total = `numTrees(1)` * `numTrees(1)` possible combinations
  3. 3 as root
     - [1,2] has `numTrees(2)` possible combinations as left subtree
     - [] has `numTrees(0)` possible combination as right subtree
     - total = `numTrees(2)` * `numTrees(0)`

we can see that this is a recursion problem and we can cache previous computed result!