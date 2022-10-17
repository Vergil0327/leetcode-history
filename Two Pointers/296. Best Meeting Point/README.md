296. Best Meeting Point

*SUBSCRIBE TO UNLOCK*

Description: [Link1](https://www.cnblogs.com/grandyang/p/5291058.html), [Link2](https://leetcode.com/discuss/interview-question/353118/Google-or-Onsite-or-Minimum-total-distance)

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

(0,0)
(0,4)
(2,2)
(0,2)

`Hint: Try to solve it in one dimension first. How can this solution apply to the two dimension case?`

```go
func minTotalDistance(grid [][]int) int {
  ROWS, COLS := len(grid), len(grid[0])

  rowList, colList := make([]int, 0), make([]int, 0)
  for r:=0; r<ROWS; r++ {
    for c:=0; c<COLS; c++ {
      if grid[r][c] == 1 {
        rowList = append(rowList, r)
        colList = append(colList, c)
      }
    }
  }

  return getMinDist(rowList) + getMinDist(colList)
}

func getMinDist(nums []int) int {
  sort.Ints(nums)

  res := 0
  l, r := 0, len(nums)-1
  for l < r {
    res += nums[r] - nums[l]
    l, r = l+1, r-1
  }
  return res
}

/*
if we want to get meeting point
and we can get distance by:

  row0, col0 := getMeetingPoint(rowList, colList)
  res := 0
  for _, r := range rowList {
    res += abs(r-rol0)
  }
  for _, c := range colList {
    res += abs(c-col0)
  }
*/
func getMeetingPoint(rowList, colList []int) (row, col int) {
  sort.Ints(rowList)
  sort.Ints(colList)

  if len(rowList)%2 == 1 {
    row = rowList[len(rowList)/2]
  } else {
    row1 := rowList[len(rowList)/2]
    row2 := rowList[len(rowList)/2 - 1]
    row = row1 + (row2-row1)/2
  }

  if len(colList)%2 == 1 {
    col = colList[len(colList)/2]
  } else {
    col1 := colList[len(colList)/2]
    col2 := colList[len(colList)/2 - 1]
    col = col1 + (col2-col1)/2
  }
  return
}
```