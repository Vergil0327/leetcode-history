# Intuition

首先得先簡化掉絕對值計算式:

We are given two numbers $a$ and $b$, with $x = |a| $, $y = |b|$, and the assumption $x \leq y$. The conditions are:

Condition 1: $\min(|a - b|, |a + b|) \leq \min(|a|, |b|)$
Condition 2: $\max(|a - b|, |a + b|) \geq \max(|a|, |b|)$

Since $x = |a|$ and $y = |b|$, and $x \leq y$, we have:

$\min(|a|, |b|) = \min(x, y) = x$
$\max(|a|, |b|) = \max(x, y) = y$

Thus, the conditions become:

Condition 1: $\min(|a - b|, |a + b|) \leq x$
Condition 2: $\max(|a - b|, |a + b|) \geq y$

### Case Analysis

##### Case 1: Both $a$ and $b$are non-negative ($a = x$, $b = y$)

$|a - b| = |x - y| = y - x$ (since $x \leq y$)
$|a + b| = |x + y| = x + y$

Compare:

Since $y - x \leq x + y$ (because $y - x \leq y + x$), we have:

- $\min(|a - b|, |a + b|) = y - x$
- $\max(|a - b|, |a + b|) = x + y$

Check conditions:

Condition 1: $\min(|a - b|, |a + b|) = y - x \leq x$

This simplifies to $y - x \leq x$, or $y \leq 2x$.


Condition 2: $\max(|a - b|, |a + b|) = x + y \geq y$

This is always true since $x \geq 0$.





So, in this case, Condition 1 gives $y \leq 2x$.

##### Case 2: $a$ non-negative, $b$ negative ($a = x$, $b = -y$)

$|a - b| = |x - (-y)| = |x + y| = x + y$
$|a + b| = |x + (-y)| = |x - y| = y - x$(since $x \leq y$)
Compare:

Since $y - x \leq x + y$, we have:

- $\min(|a - b|, |a + b|) = y - x$
- $\max(|a - b|, |a + b|) = x + y$




Check conditions:

Condition 1: $y - x \leq x$, or $y \leq 2x$

Condition 2: $x + y \geq y$, which is true.



Again, Condition 1 gives $y \leq 2x$.

##### Case 3: $a$ negative, $b$ non-negative ($a = -x $, $b = y$)

$|a - b| = |-x - y| = x + y$
$|a + b| = |-x + y| = |y - x| = y - x $(since $x \leq y$)
Compare:

- $\min(|a - b|, |a + b|) = y - x$
- $\max(|a - b|, |a + b|) = x + y$


Check conditions:

Condition 1: $y - x \leq x$, or $y \leq 2x$

Condition 2: $x + y \geq y$, which is true.



Condition 1 consistently gives $y \leq 2x$.

##### Case 4: Both negative ($a = -x $, $b = -y$)

$|a - b| = |-x - (-y)| = |-x + y| = |y - x| = y - x$
$|a + b| = |-x - y| = x + y$
Compare:

- $\min(|a - b|, |a + b|) = y - x$
- $\max(|a - b|, |a + b|) = x + y$


Check conditions:

Condition 1: $y - x \leq x$, or $y \leq 2x$

Condition 2: $x + y \geq y$, which is true.

結論: 假設 x <= y; 合法條件能簡化成`y <= 2*x`
因此對nums以絕對值做排序後, 用sliding window找出合法範圍即可
