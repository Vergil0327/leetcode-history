class SmallestInfiniteSet {
public:
    set<int> available;  // Available numbers to pop
    int nextNum;         // Next number in the infinite sequence
    
    SmallestInfiniteSet() {
        nextNum = 1;
    }
    
    int popSmallest() {
        if (available.empty()) {
            // No previously added back numbers, return next in sequence
            return nextNum++;
        } else {
            // Return smallest from available set
            int smallest = *available.begin();
            available.erase(available.begin());
            return smallest;
        }
    }
    
    void addBack(int num) {
        if (num < nextNum) {
            available.insert(num);
        }
        // If num >= nextNum, it's already "available" in the infinite sequence
    }
};