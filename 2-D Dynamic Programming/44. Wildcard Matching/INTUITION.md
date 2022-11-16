#### Intuition

discuss case by case

define dfs(i, j) is we try to match s[i:] with p[j:]

If...

1. s[i] equals to p[j], keep match rest of string, s[i+1:] with p[j+1:]
2. s[i] NOT equals to p[j], s[i:] can't matched with p[j:]
3. p[j] is "?", same situation with 1.
4. p[j] is "*"
   1. we can use it to match s[i] and keep matching rest of substring. s[i+1:] with p[j:]
   2. **BUT** we also can choose **NOT** to use "*" and keep matching rest of substring. s[i:] with p[j+1:]