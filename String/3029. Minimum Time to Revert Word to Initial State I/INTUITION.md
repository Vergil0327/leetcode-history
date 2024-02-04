# Intuition

example1.
abacaba
t=1: aba | caba + bac
t=2: cab | abac + aba
abacaba

suffix我們可以任意組成不管, 我們在意的是每次操作後剩下的prefix能不能跟任意組成的suffix組成原本的word

所以每次操作都相當於:

t=1, prefix = word[k:]
t=2, prefix = word[k*2:]
at time = t, prefix = word[k*t:]
一但prefix == word[:len(prefix)], 我們就能停止
如果一直都沒找到, 由於suffix可以任意組成, 最終也肯定能組成一開始的word