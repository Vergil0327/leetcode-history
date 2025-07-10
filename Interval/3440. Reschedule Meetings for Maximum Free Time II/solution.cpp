class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        
        // Edge case: no events
        if (n == 0) return eventTime;
        
        // Step 1: Calculate gaps between consecutive events
        vector<int> gaps;
        gaps.reserve(n + 1); // Reserve space for efficiency
        
        // First gap: from 0 to first event start
        gaps.push_back(startTime[0]);
        
        // Middle gaps: between consecutive events
        for (int i = 1; i < n; i++) {
            gaps.push_back(startTime[i] - endTime[i-1]);
        }
        
        // Last gap: from last event end to total time
        gaps.push_back(eventTime - endTime[n-1]);
        
        // Step 2: Build prefix and suffix maximum arrays more efficiently
        vector<int> prefixMax(n + 2, 0);  // prefixMax[i] = max of gaps[0..i-1]
        for (int i = 0; i <= n; i++) {
            prefixMax[i + 1] = max(prefixMax[i], gaps[i]);
        }
        
        vector<int> suffixMax(n + 2, 0);  // suffixMax[i] = max of gaps[i..n]
        for (int i = n; i >= 0; i--) {
            suffixMax[i] = max(suffixMax[i + 1], gaps[i]);
        }
        
        // Step 3: Find maximum free time
        int res = *max_element(gaps.begin(), gaps.end());  // Strategy 1: largest single gap
        
        // Strategy 2: Try modifying each event
        for (int i = 0; i < n; i++) {
            int duration = endTime[i] - startTime[i];
            
            // Option 2a: Cancel event i (merge adjacent gaps)
            int mergedGap = gaps[i] + gaps[i + 1];
            res = max(res, mergedGap);
            
            // Option 2b: Move event i to another location
            // Find the largest gap outside of gaps[i] and gaps[i+1]            
            // Only move if the event can fit in another gap
            if (max(prefixMax[i], suffixMax[i + 2]) >= duration) {
                res = max(res, mergedGap + duration);
            }
        }
        
        return res;
    }
};

/* 
Visualization of the algorithm:

Original timeline:
[0] <gap1> [event1] <gap2> [event2] <gap3> [event3] <gap4> [eventTime]

Strategy 1: Use largest single gap
Answer = max(gap1, gap2, gap3, gap4)

Strategy 2a: Cancel an event (e.g., event2)
[0] <gap1> [event1] <gap2+gap3> [event3] <gap4> [eventTime]
Answer = gap2 + gap3

Strategy 2b: Move an event (e.g., move event2 to gap4 if it fits)
[0] <gap1> [event1] <gap2+gap3> [event3] <gap4-event2_duration> [event2] [eventTime]
Answer = gap2 + gap3 + event2_duration

The algorithm uses prefix/suffix max arrays to efficiently check if an event 
can be moved to any other gap without having to check each gap individually.
*/

/*
COMPLEXITY:
- Time: O(n) - single pass through events
- Space: O(n) - for gaps and prefix/suffix arrays

The algorithm correctly handles all three strategies:
1. Use largest existing gap
2. Cancel an event to merge adjacent gaps  
3. Move an event to create maximum continuous free time
*/