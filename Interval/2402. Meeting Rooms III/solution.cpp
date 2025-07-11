#define pli pair<long long,int>
class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());

        priority_queue<int, vector<int>, greater<int>> available;
        for (int room=0; room<n; room++) {
            available.push(room);
        }
        
        long long t = 0;
        vector<int> count(n, 0);
        priority_queue<pli, vector<pli>, greater<pli>> occupied; // [end_time, room_id]
        for (int i=0; i<meetings.size(); i++) {
            int start=meetings[i][0], end=meetings[i][1];
            t = max(t, (long long)start);

            while (!occupied.empty() && occupied.top().first <= start) {
                auto [end_time, room] = occupied.top();
                occupied.pop();
                available.push(room);
            }

            int duration = end-start;
            if (!available.empty()) {
                int room = available.top();
                available.pop();

                count[room]++;
                occupied.push({t + duration, room});
            } else {
                auto [end_time, room] = occupied.top();
                occupied.pop();

                t = max(t, end_time);
                count[room]++;
                occupied.push({t + duration, room});
            }
        }

        // int mx_room = 0;
        // for (int i=1; i<n; i++) {
        //     if (count[i] > count[mx_room]) {
        //         mx_room = i;
        //     }
        // }
        // return mx_room;
        auto iter = max_element(count.begin(), count.end());
        return distance(count.begin(), iter);
    }
};

