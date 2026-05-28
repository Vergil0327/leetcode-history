#include <vector>

using namespace std;

class Solution {
    struct TrieNode {
        // 儲存子節點在 vector 中的索引，0 代表沒有子節點
        int next[26];
        // 儲存通過目前節點（共享目前字尾）的最優 wordsContainer 字串索引
        int best_idx;
        
        TrieNode() {
            fill(begin(next), end(next), 0);
            best_idx = -1;
        }
    };

    vector<TrieNode> trie;

    // 輔助函式：用來比較兩個字串誰更優（更短，或相同長度下索引更小）
    bool isBetter(int new_idx, int old_idx, const vector<string>& wordsContainer) {
        if (old_idx == -1) return true;
        if (wordsContainer[new_idx].size() != wordsContainer[old_idx].size()) {
            return wordsContainer[new_idx].size() < wordsContainer[old_idx].size();
        }
        return new_idx < old_idx;
    }

    void insert(const string& s, int words_idx, const vector<string>& wordsContainer) {
        int curr = 0; // 根節點的索引是 0
        
        // 根節點本身也要維護完全沒有共同字尾時的最優解
        if (isBetter(words_idx, trie[curr].best_idx, wordsContainer)) {
            trie[curr].best_idx = words_idx;
        }

        // 從後往前插入字元（因為是找字尾 Suffix）
        for (int i = s.size() - 1; i >= 0; --i) {
            int c = s[i] - 'a';
            if (trie[curr].next[c] == 0) {
                trie.push_back(TrieNode());
                trie[curr].next[c] = trie.size() - 1;
            }
            curr = trie[curr].next[c];
            
            // 關鍵優化：在走訪路徑時，即時更新該節點的最優解
            if (isBetter(words_idx, trie[curr].best_idx, wordsContainer)) {
                trie[curr].best_idx = words_idx;
            }
        }
    }

public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        trie.clear();
        trie.push_back(TrieNode()); // 插入根節點 (index 0)

        // 1. 建樹：將所有貨櫃字串逆序插入
        for (int i = 0; i < wordsContainer.size(); ++i) {
            insert(wordsContainer[i], i, wordsContainer);
        }

        // 2. 查詢：走訪 Query
        vector<int> ans;
        for (const string& q : wordsQuery) {
            int curr = 0;
            int last_valid_idx = trie[0].best_idx; // 預設為全域最優解

            for (int i = q.size() - 1; i >= 0; --i) {
                int c = q[i] - 'a';
                if (trie[curr].next[c] != 0) {
                    curr = trie[curr].next[c];
                    last_valid_idx = trie[curr].best_idx; // 只要能往下走，就更新當前最長匹配字尾的最優解
                } else {
                    break; // 無法繼續匹配，直接中斷
                }
            }
            ans.push_back(last_valid_idx);
        }

        return ans;
    }
};