737. Sentence Similarity II

*[SUBSCRIBE TO UNLOCK](https://leetcode.com/problems/sentence-similarity-ii/)*

Given two sentences `words1`, `words2` (each represented as an array of strings), and a list of similar word pairs `pairs`, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if “great” and “good” are similar, and “fine” and “good” are similar, then “great” and “fine” are similar.

Similarity is also symmetric. For example, “great” and “fine” being similar is the same as “fine” and “great” being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

- The length of words1 and words2 will not exceed 1000.
- The length of pairs will not exceed 2000.
- The length of each pairs[i] will be 2.
- The length of each words[i] and pairs[i][j] will be in the range [1, 20].

<details>
<summary>Solution</summary>

[HuaHua](https://zxi.mytechroad.com/blog/hashtable/leetcode-737-sentence-similarity-ii/)
[Other](https://www.cnblogs.com/grandyang/p/8053934.html)

</details>

```go
func areSentencesSimilarTwo(words1, words2 []string, pairs [][2]string) bool {
  if len(words1) != len(words2) {
    return false
  }

  parent := map[string]string{}

  var find = func(word string) string {
    if _, ok := parent[word]; !ok {
      parent[word] = word
      return word
    }

    p := parent[word]
    for p != parent[p] {
      parent[p] = parent[parent[p]]
      p = parent[p]
    }

    return p
  }

  // construct Union-Find Disjoint Set
  for _, pair := range pairs {
    left, right := pair[0], pair[1]
    pl, pr := find(left), find(right)

    if pl != pr {
      parent[pl] = pr // union
    }
  }

  for i, word := range words1 {
    if find(word) != find(words2[i]) {
      return false
    }
  }

  return true
}
```