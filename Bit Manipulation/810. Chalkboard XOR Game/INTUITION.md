# Intuition

觀察題, 像是腦筋急轉彎的題目

first of all:

`XOR = Num1^Num2^Num3^...^NumN`

if XOR is already 0 at first, alice win.

then we discuss how to win:

now `XOR != 0`, then we want to remove NumI and XOR^NumI != 0

if we can't find this specific NumI to remove, which means XOR^NumI == 0,
it means only 1 distinct num left in nums, we can't win.

that is, if we has just 2 distinct num, we already win.

if we has more than 2 distinct num, we won't lose at this turn, and we take turns to remove distinct num.

every even numbers of nums[i] don't matter, we'll take turns and safely to remove any one of distinct number, see below:

we can safely to remove X, Y alternately
- X Y XXXX YYYY
- X Y Z XXXX YYYY ZZZZ

thus, let's discuss:
1. X => lose
2. X Y => already win
3. X Y Z => alread lose
4. W X Y Z => already win

we can see that if nums.length == 0 and xor != 0, alice will win.

edge case: what if 0 in nums?

1. 0 X => alice win after remove 0
2. 0 0 X or 0 X Y => alice lose no matter how she remove.
    - if alice remove 0 first, then bob can remove 0 too. in the end, remain 1 distinct num for alice
    - if alice remove distinct num first, bob can remove distinct num too. in the end remain 0 and XOR == 0 for alice

therefore, alice only win if she has even number of nums