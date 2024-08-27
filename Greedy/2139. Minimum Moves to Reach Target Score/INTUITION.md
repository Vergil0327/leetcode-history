# Intuition

double越後面用越有效益:
1*2 = 2
2*2 = 4
4*2 = 8
8*2 = 16
所以我們從target往start往回, greedily apply double operation back
等到maxDoubles用完, 剩下就是increment operations