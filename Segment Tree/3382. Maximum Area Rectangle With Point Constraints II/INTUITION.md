# Intuition

1. Sort the point by x, for the same x, sort by y.
2. `yMax` stores the previous max `x` value for each `y`.
   - This represents the x-coordinate of the most recent point that has the same y value as y.
   - It keeps track of the leftmost x-coordinate along the horizontal line defined by y
3. To identify an axis-aligned rectangle with no other points on the border: prevX == x and yMax[prevY] == yMax[y]. Top and bottom borders: y and prevY; Left and right borders: yMax[y] and x.
4. Use a Segment Tree maxTree to maintain the max values in `yMax`. To determine if the rectangle doesn't contain any other points, the max `x` values in `yMax` between `prevY` and `y` should be less than the left border `yMax[y]`: yMax[y] > maxTree.query(yPos[prevY], yPos[y]).
   - maxTree.query(yPos[prevY], yPos[y]):
     1. This finds the maximum x-coordinate of any point in the range of y-values between prevY and y (inclusive).
     2. The SegmentTree is used to efficiently compute this maximum value
   - The Rectangle, The current rectangle is defined by four points:
     1. (yMax[prevY], prevY): The bottom-left corner.
     2. (yMax[y], y): The top-left corner.
     3. (x, prevY): The bottom-right corner.
     4. (x, y): The top-right corner.
   - To check whether any point lies inside this rectangle: A point is considered "inside" if its x-coordinate is strictly **less than** x and strictly **greater than** prev closest X (== yMax[prevY] == yMax[y]), and its y-coordinate is between prevY and y.
     - see `maxTree.query(yPos[prevY], yPos[y])`:
5. To fit the y-axis into the segment tree, compress the y values and assign an index for each distinct y value (see yAxis and yPos).

示意圖:
所以如果[prevY,y]這範圍內都沒有任何一個`x`位置超過 yMax[y], 那代表當前矩形內沒有任何的點
所以才用 segment tree 去維護兩段(prevY, y)內的 max `x` position

```
-----------------------------------------------(x,y)
                   |                            |
                   |                            |
                   |                            |
-----------(yMax[prevY] prevY)-------------------
```

# Problem Breakdown

The task is to find the maximum rectangle area where:

1. The rectangle is axis-aligned.
2. Four points form the corners of the rectangle.
3. No points lie inside or on the border of the rectangle.
   The key challenge lies in efficiently checking whether points inside a candidate rectangle violate the conditions (i.e., lie inside or on its border).

# Approach

### Step 1: Sorting and Preprocessing

- **Sort points by x and y:**

```py
points.sort()
```

Sorting the points by x (and then by y for ties) allows us to iterate through potential rectangles systematically, starting with the leftmost and moving right.

- **Extract unique y values and map them to indices:**

```python
yAxis = sorted(set(yCoord))
yPos = {y: i for i, y in enumerate(yAxis)}
```

This step compresses the y coordinates into a smaller index space, reducing the dimensionality for the Segment Tree.

### Step 2: Maintaining Maximum x Values

- **Track the maximum x for each y using a dictionary (yMax):**

```py
yMax = {y: -inf for y in yAxis}
```

This helps identify candidate rectangles with aligned y-coordinates quickly.

- **Use a Segment Tree to support range queries:**

The Segment Tree is used to query the maximum x value in a range of y indices (yPos[prevY] to yPos[y]). This ensures efficient validation of rectangles.

### Step 3: Iterating Through Points

- As we iterate through sorted points:

```python

for x, y in points[1:]:
```

Each point (x, y) is treated as the potential top-right or bottom-right corner of a rectangle. The logic checks if a valid rectangle can be formed with aligned points.

### Step 4: Rectangle Validation

The conditions for forming a valid rectangle are as follows:

1. **Aligned x and y values:**

```python
if prevX == x and yMax[prevY] == yMax[y]:
```

This ensures that the current point (x, y) and its potential counterpart (prevX, prevY) are aligned along both axes.

2. **Maximum x values along the y-range:**

```python

if yMax[y] > maxTree.query(yPos[prevY], yPos[y]):
```

This checks whether any point inside the rectangle exceeds the rectangle's boundary conditions. If no point inside violates the constraints, the rectangle is valid.

3. **Calculate the area:**

```python
res = max(res, (y-prevY) * (x - yMax[y]))
```

If the rectangle is valid, compute its area and update the result.

# Intuition Behind the Key Condition

```python
if prevX == x and yMax[prevY] == yMax[y] and yMax[y] > maxTree.query(yPos[prevY], yPos[y]):
```

This condition ensures that:

1. Points align on both axes: prevX == x ensures alignment along x, and yMax[prevY] == yMax[y] ensures alignment along y.
2. No points inside violate the rectangle: yMax[y] > maxTree.query(yPos[prevY], yPos[y]) checks that no points inside the rectangle.

### Step 5: Update State

After processing a point (prevX, prevY):

1. Update yMax with the current prevX for the y coordinate:

```python
yMax[prevY] = max(yMax[prevY], prevX)
```

2. Update the Segment Tree:

```python
maxTree[yPos[prevY]] = yMax[prevY]
```
