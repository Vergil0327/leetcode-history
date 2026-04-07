#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Robot {
private:
    int w, h;
    int x, y;
    int dx, dy;
    bool moved;

    // Directions: 0: East, 1: North, 2: West, 3: South
    string dirNames[4] = {"East", "North", "West", "South"};

public:
    Robot(int width, int height) {
        w = width;
        h = height;
        x = 0;
        y = 0;
        dx = 1; // Start East
        dy = 0;
        moved = false;
    }
    
    void step(int num) {
        int perimeter = 2 * (w + h) - 4;
        num %= perimeter;
        
        // If we move a multiple of the perimeter, we are back at (0,0)
        // but the direction must reflect that we just "arrived" there from the South.
        if (num == 0) moved = true; 

        while (num > 0) {
            moved = true;
            if (dx == 1 && dy == 0) { // East
                int steps = min(num, w - 1 - x);
                x += steps;
                num -= steps;
                if (num > 0 && x == w - 1) { dx = 0; dy = 1; } // Turn North
            } 
            else if (dx == 0 && dy == 1) { // North
                int steps = min(num, h - 1 - y);
                y += steps;
                num -= steps;
                if (num > 0 && y == h - 1) { dx = -1; dy = 0; } // Turn West
            } 
            else if (dx == -1 && dy == 0) { // West
                int steps = min(num, x);
                x -= steps;
                num -= steps;
                if (num > 0 && x == 0) { dx = 0; dy = -1; } // Turn South
            } 
            else if (dx == 0 && dy == -1) { // South
                int steps = min(num, y);
                y -= steps;
                num -= steps;
                if (num > 0 && y == 0) { dx = 1; dy = 0; } // Turn East
            }
        }

        // Special case for (0,0): If we have completed a full loop, 
        // the direction should be South (as if we just finished the lap).
        if (x == 0 && y == 0 && moved) {
            dx = 0;
            dy = -1;
        }
    }
    
    vector<int> getPos() {
        return {x, y};
    }
    
    string getDir() {
        if (dx == 1) return "East";
        if (dy == 1) return "North";
        if (dx == -1) return "West";
        return "South";
    }
};