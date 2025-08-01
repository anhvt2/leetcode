#include <iostream>
#include <queue>
using namespace std;

class HitCounter {
private:
    queue <pair<int, int>> hits; // {timestamp, count}
    int totalHits = 0;

public:
    HitCounter() {}
   
    void hit(int timestamp) {
        if (!hits.empty() && hits.back().first == timestamp) {
            hits.back().second++; // Same timestamp as last hit: just increment count
        }
        else {
            hits.push({timestamp, 1}); // New timestamp: add new entry to queue
        }
        totalHits++;
    }
    
    int getHits(int timestamp) {
        // Remove hits older than 5 minutes
        while (!hits.empty() && hits.front().first <= timestamp - 300) {
            totalHits -= hits.front().second; // Subtract expired hits
            hits.pop(); // Remove outdated timestamp
        }
        return totalHits;
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */