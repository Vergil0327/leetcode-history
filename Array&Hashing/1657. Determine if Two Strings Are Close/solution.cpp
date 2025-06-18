class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int count1[26], count2[26];
        for (char ch : word1) {
            count1[ch-'a']++;
        }
        for (char ch : word2) {
            count2[ch-'a']++;
        }

        unordered_map<int,int> occurence;
        for (int ch=0; ch<26; ch++) {
            if (count1[ch] == 0 && count2[ch] != 0) return false;
            if (count1[ch] != 0 && count2[ch] == 0) return false;
            if (count1[ch] == count2[ch]) continue;

            // check op.2 feasibility
            occurence[count1[ch]] += 1;
            occurence[count2[ch]] -= 1;
        }

        for (auto& it : occurence) {
            if (it.second != 0) return false;
        }

        return true;
    }
};