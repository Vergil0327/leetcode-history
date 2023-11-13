# Intuition

首先想到的是:

總共26個字母, 如果用個26-bit length的bitmask當作state的話
可以把每個words[i]轉成一個長度26-bit的bitmask
同樣puzzles[i]也可轉成長度為26的bitmask
只要words[i].bit_mask & puzzles[i].bit_mask == words[i].bit_mask
這就代表words[i]可用puzzles[i]組出來

所以這題需要的是該如何高效搜索出words[i]是不是puzzles[i]的submask
所以首先想到的是把所有words[i]轉為bitmask後, 放入hashmap裡計數
```py
counter = defaultdict(int)
for word in words:
    bit = 0
    for ch in set(word):
        bit |= 1<<(ord(ch)-ord("a"))

    counter[bit] += 1
```

然後在遍歷puzzles[i]並轉為bitmask, 轉換完後再透過以下技巧遍歷submask:

```py
state = some bitmask
submask = state
while submask > 0:
    # do your thing to valid submask here
    submask = (submask-1)&state
```

由於第一個規則說明submask必須包含puzzles[i]的首位字母, 也就是puzzles[i][0]
所以我們只有當`submask contains first_puzzle_letter`時可以`res[i] += counter[submask]`

# Other Solution - Trie

```java
class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        Trie root = new Trie();
        for (String word : words){
            char[] cs = word.toCharArray();
            Arrays.sort(cs);
            StringBuffer sb = new StringBuffer();
            sb.append(cs[0]);
            for (int i=1;i<cs.length;i++){
                if (cs[i]!=cs[i-1])sb.append(cs[i]);
            }
            addWord(sb.toString(), root);
        }
        List<Integer> list = new ArrayList<>();
        for (String puzzle : puzzles){
            list.add(search(puzzle, root,  'a'));
        }
        return list;
    }


    private int search(String puzzle, Trie cur, char start){
        int count = 0;
        if (cur.word!=null && cur.word.indexOf(puzzle.charAt(0))!=-1){
            count+=cur.count;
        }
        for (char c = start; c<='z';c++){
            if (cur.children[c-'a']!=null && puzzle.indexOf(c)!=-1){
                count+=search(puzzle, cur.children[c-'a'], (char)(c+1));
            }
        }
        return count;
    }




    private void addWord(String word, Trie root){
        Trie cur = root;
        for (int i=0;i<word.length();i++){
            int j = word.charAt(i)-'a';
            if (cur.children[j]==null){
                cur.children[j] = new Trie();
            }
            cur = cur.children[j];
        }
        cur.word = word;
        cur.count++;
    }



    class Trie{
        Trie[] children = new Trie[26];
        String word = null;
        int count = 0;
    }
}
```