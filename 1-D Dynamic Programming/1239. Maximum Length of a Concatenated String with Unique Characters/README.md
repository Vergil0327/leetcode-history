[1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

`Medium`

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

```
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
```

Constraints:

- 1 <= arr.length <= 16
- 1 <= arr[i].length <= 26
- arr[i] contains only lowercase English letters.

<details>
<summary>Hint 1</summary>

You can try all combinations and keep mask of characters you have.
</details>

<details>
<summary>Hint 2</summary>

You can use DP.
</details>

<details>
<summary>Solution</summary>

[here](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/2739812/Golang-Python-Bottom-Up-Top-Down-DP-Solution-Daily-Challenge)
</details>

<details>
<summary>Python Solution</summary>

[bit & set operations](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/2737493/PythonC%2B%2BJavaRust-0-ms-bit-and-set-operations-(with-detailed-comments))
</details>

<details>
<summary>Golang Solution</summary>

[Golang DFS w/t Mask Solution](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/2739819/Golang-Simple-Count-bits-in-bitMask)

```go
func maxLength(arr []string) int {
    masks := []uint32{}
    
    res := 0
    for _, word := range arr {
        if mask, ok := getMask(word); ok {
             masks = append(masks, mask)
        }       
    }
    
    dfs(masks, 0, 0, &res)
    return res
}

func dfs(masks []uint32, index int, mask uint32, res *int) {
    *res = max(*res, countOnes(mask))
    
    for i := index; i < len(masks); i++ {
        if mask & masks[i] == 0 {  // If no overlap
            dfs(masks, i + 1, mask | masks[i], res)
        }
    }
}

func countOnes(mask uint32) int {
    count := 0
    for i := 0; i < 26; i++ {
        if mask & (1 << i) != 0 {
            count++
        }
    }
    return count
}

func getMask(word string) (uint32, bool) {
    var mask uint32
    
    for _, c := range word {
        if mask & (1 << (c - 'a')) != 0 {
            // repeated characters
            return 0, false
        }
        mask |= 1 << (c - 'a')
    }
    return mask, true
}

func max(a, b int) int {
    if a > b { 
        return a 
    }
    return b
}
```
</details>