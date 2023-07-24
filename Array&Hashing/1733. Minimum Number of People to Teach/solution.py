class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        langs = [set(lang) for lang in languages]
        need_to_teach = []
        for u, v in friendships:
            i, j = u-1, v-1
            
            if len(langs[i] & langs[j])>0:
                continue
            need_to_teach.append([u,v])
        
        res = inf
        for teached_lang in range(1, n+1):
            learned = langs.copy()
            teached = 0

            for u, v in need_to_teach:
                i, j = u-1, v-1
                
                if teached_lang not in learned[i]:
                    learned[i].add(teached_lang)
                    teached += 1
                if teached_lang not in learned[j]:
                    learned[j].add(teached_lang)
                    teached += 1
            
            res = min(res, teached)
        return res