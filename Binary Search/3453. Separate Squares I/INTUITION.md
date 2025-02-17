# Intuition

直覺想到用binary search去找出答案那條線, 要注意的是浮點數(floating number)的大小比較
binary search退出條件改成`while r-l >= 1e-5:` (因為題目說明答案差值小於1e-5時可被接受)