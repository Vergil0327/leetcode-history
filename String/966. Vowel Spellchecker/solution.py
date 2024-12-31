class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # word to index
        case_insensitive = {}
        word_dict = {}
        vowel_err = {}
        
        def replace_vow(s):
            for v in {"a", "e", "i", "o", "u"}:
                s = s.replace(v, "#")
            return s

        for i, word in enumerate(wordlist):
            word_dict[word] = i
            if word.lower() not in case_insensitive:
                case_insensitive[word.lower()] = i
            
            s = replace_vow(word.lower())
            if s not in vowel_err:
                vowel_err[s] = i

        res = []
        for q in queries:
            if q in word_dict:
                res.append(q)
            elif (s := q.lower()) in case_insensitive:
                res.append(wordlist[case_insensitive[s]])
            elif (s := replace_vow(q.lower())) in vowel_err:
                res.append(wordlist[vowel_err[s]])
            else:
                res.append("")
        return res
