// great solution in terms of time and space
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> answer;
        int left = 0;
        int right = products.size()-1;
        sort(products.begin(), products.end());
        for(int i = 0; i < searchWord.size(); i++){
            char currChar = searchWord[i];
            while(left <= right && (products[left].length() <= i || products[left][i] != currChar)){
                left++;
            }
            while(right >= left && (products[right].length() <= i || products[right][i] != currChar)){
                right--;
            }
            int range = right - left + 1;
            answer.push_back({});
            for(int j = 0; j < min(3, range); j++){
                answer[answer.size()-1].push_back(products[left+j]);
            }
        }


        return answer;
    }
};