class Trie {
private:
    class TrieNode {
    public:
        TrieNode* next[26];
        bool isEnd;

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
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (auto& c : prefix) {
            if (node->next[c-'a'] == NULL) return false;
            node = node->next[c-'a'];
        }
        return true;
    }
};