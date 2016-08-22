/*
    Problem: Moving Average From Data Stream
    (https://leetcode.com/problems/moving-average-from-data-stream/)
*/

#include <queue>

class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) : maxWindowSize(size), currentWindowAverage(0) {}
    
    double next(int val) {
        // window already max size, slide
        if (maxWindowSize == window.size()) {
            slide(val);
        } else {
            growWindowRight(val);
        }
        return currentWindowAverage;
    }


private:
    void growWindowRight(int val) {
        double windowSum = currentWindowAverage*window.size();
        currentWindowAverage = (windowSum + val)/(window.size() + 1.0);
        window.push(val);
    }

    void shrinkWindowLeft() {
        double removedOldestReading = currentWindowAverage - window.front()/(window.size()*1.0);
        // divide by 0 possibility 
        if ((window.size() - 1) == 0) {
            currentWindowAverage = 0.0;
        } else {
            currentWindowAverage = removedOldestReading*window.size()/(window.size() - 1.0);
        }
        window.pop();
    }

    void slide(int val) {
        shrinkWindowLeft();
        growWindowRight(val);
    }

    std::queue<int> window;
    int maxWindowSize;
    double currentWindowAverage;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */