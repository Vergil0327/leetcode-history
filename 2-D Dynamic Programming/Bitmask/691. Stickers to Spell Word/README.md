[691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/description/)

`Hard`

We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return `-1`.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

```
Example 1:
Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:
Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
```

Constraints:

- n == stickers.length
- 1 <= n <= 50
- 1 <= stickers[i].length <= 10
- 1 <= target.length <= 15
- stickers[i] and target consist of lowercase English letters.

<details>
<summary>Hint</summary>

We want to perform an exhaustive search, but we need to speed it up based on the input data being random. For all stickers, we can ignore any letters that are not in the target word. When our candidate answer won't be smaller than an answer we have already found, we can stop searching this path. When a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection. [Here, we say a sticker `A` dominates `B` if `A.count(letter) >= B.count(letter)` for all letters.]

</details>

<details>
<summary>Solution w/t Explanation</summary>

[Neetcode - topdown](https://www.youtube.com/watch?v=hsomLb6mUdI&ab_channel=NeetCode)

[HuifengGuan - bottomup](https://www.youtube.com/watch?v=QusReweeTqI&ab_channel=HuifengGuan)
</details>