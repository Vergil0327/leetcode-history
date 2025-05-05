# Intuition

We can use a divide and conquer approach to solve.

The problem requires a special grid to basically always be increasing in a spiral direction from `top-right` -> `bottom-right` -> `bottom-left` -> `top-left`.

If we recursively solve each each quadrant while using a global counter from zero we can fill the grid will maintaining the special property. We would just need to ensure our recursive calls are **in correct order**.