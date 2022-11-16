### Top-Down

Since **`*`** is tricky part in this problem, we discuss it separately

#### Case by case:

Lets compare `s[i:]` with `p[j:]` recursively. (dynamic programming way)

1. if `p[j+1]` equals to **`*`**:
   1.  we can use **`*`** with preceding character to match `s[i]`
   2.  we can also **NOT** to use **`*`** to match, we take it as zero times and keep compare `s[i:]` with rest of `p[j+2:]`

2. if `p[j+1]` **NOT** equals to **`*`**:
   -  it's just simple string matching, just like [Leetcode 44 Wildcaard Matching](../44.%20Wildcard%20Matching/)

#### Base Case

- if `s[i:]` == "" and `p[j:]` = "", `p[j:]` matches with `s[i:]`
- if `s[i:]` == "XXXXX" and `p[j:]` = "", `p[j:]` is **impossible** to match `s[i:]`

- if `s[i:]` == "" and `p[j:]` = "XXXXXX",

still discuss with **`*`** and **NOT** with **`*`**

  - if `p[j+1]` is **`*`**, we can see it as `p[j]` matches zero times, and keep comparing `s[i:]` with `p[j+2:]`
    - thinks these case
    - s = "" and p = ".*"
    - s = "" and p = ".*a"
  - else we just can't matches s with p
    - s = "" and p = "a"