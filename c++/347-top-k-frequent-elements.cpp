#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;

        // Step 1: Count frequencies
        for (int num: nums) {
            freqMap[num]++;
        }

        // Step 2: min-heap of (frequency, num)
        priority_queue<pair<int, int>, vector<pair <int, int>>, greater<>> minHeap;
        
        for (auto& [num, freq]: freqMap) {
            minHeap.push({freq, num});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }

        // Step 3: Extract elements from heap
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return result;
    }
};
