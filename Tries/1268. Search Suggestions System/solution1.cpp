// leetcode 208
class Trie {
private:
    class TrieNode {
    public:
        TrieNode* next[26];
        bool isEnd;
        vector<string> list;

        TrieNode() {
            for (int i=0; i<26; i++) {
                next[i] = NULL;
            }
            isEnd = false;
        }
    };
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (auto& c : word) {
            int key = c-'a';
            if (node->next[key] == NULL) {
                node->next[key] = new TrieNode();
            }
            node = node->next[key];
            node->list.push_back(word);
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (auto& c : word) {
            if (node->next[c-'a'] == NULL) return false;
            node = node->next[c-'a'];
        }
        return node->isEnd;
    }
    
    vector<string> startsWith(string prefix) {
        TrieNode* node = root;
        for (auto& c : prefix) {
            if (node->next[c-'a'] == NULL) return {};
            node = node->next[c-'a'];
        }

        return node->list;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        Trie* root = new Trie();

        sort(products.begin(),products.end());
        for (auto& product : products) {
            root->insert(product);
        }

        vector<vector<string>> res;
        string prefix = "";
        for (auto& ch : searchWord) {
            prefix += ch;
            vector<string> candidates = root->startsWith(prefix);

            // take top 3 suggestions
            vector<string> first3(
                candidates.begin(),
                candidates.begin() + min(3, (int)candidates.size())
            );

            res.push_back(first3);
        }
        return res;
    }
};