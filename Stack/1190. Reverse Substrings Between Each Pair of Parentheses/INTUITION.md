# Intuition

看到左右括號, 先想到遞歸或是stack (iterative way)

依照題意, 分出三種情況:
1. s[i] == "("
2. s[i] == ")"
3. s[i].isalpha()

再依據題意, 在遇到右括號")"時，反轉即可