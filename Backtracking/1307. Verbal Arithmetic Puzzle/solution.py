class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        result = result[::-1]
        for i in range(len(words)):
            if len(words[i]) > len(result): return False
            words[i] = words[i][::-1]

        decode = [-1]*26
        used = [0]*10
        key = lambda x: ord(x)-ord("A")

        def dfs(i, j, total):
            if j == len(result):
                if len(result) > 1 and decode[key(result[i-1])] == 0: # leading zero
                    return False
                
                return total == 0

            if i == len(words):
                char = key(result[j])
                
                if decode[char] != -1:
                    if decode[char] != total%10:
                        return False
                    else:
                        return dfs(0, j+1, total//10)
                else:
                    if used[total%10]: return False

                    decode[char] = total%10
                    used[total%10] = 1
                    if dfs(0, j+1, total//10): return True
                    decode[char] = -1
                    used[total%10] = 0
                    return False
            
            if j >= len(words[i]):
                return dfs(i+1, j, total)

            ch = key(words[i][j])
            if decode[ch] != -1:
                if len(words[i]) > 1 and i == len(words[i])-1 and decode[ch] == 0: # leading zero
                    return False
                return dfs(i+1, j, total + decode[ch])
            else:
                for d in range(10):
                    if used[d]: continue
                    if len(words[i]) > 1 and i == len(words[i])-1 and d == 0: continue # leading zero

                    decode[ch] = d
                    used[d] = 1
                    if dfs(i+1, j, total + decode[ch]): return True
                    decode[ch] = -1
                    used[d] = 0
                return False
        return dfs(0, 0, 0)
