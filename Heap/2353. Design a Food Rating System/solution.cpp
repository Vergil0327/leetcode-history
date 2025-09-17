using pis = pair<int,string>;
class FoodRatings {
public:
    int n;
    unordered_map<string,int> rating;
    unordered_map<string, string> foodToCuisine;
    unordered_map<string, priority_queue<pis, vector<pis>, decltype([](const pis& a, const pis& b) -> bool {
    if (a.first == b.first) return a.second > b.second;
    return a.first < b.first;
})>> m;
    
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        n = foods.size();

        for (int i=0; i<n; i++) {
            rating[foods[i]] = ratings[i];
            foodToCuisine[foods[i]] = cuisines[i];
            m[cuisines[i]].push({ratings[i], foods[i]});
        }
    }
    
    void changeRating(string food, int newRating) {
        rating[food] = newRating;
        m[foodToCuisine[food]].push({newRating, food}); // Add new entry
    }
    
    string highestRated(string cuisine) {
        while (!m[cuisine].empty() && 
               m[cuisine].top().first != rating[m[cuisine].top().second]) {
            m[cuisine].pop();
        }
        return m[cuisine].top().second;
    }
};