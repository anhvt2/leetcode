#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map; // Map to store number and its index
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i]; // The number we need to find
            if (map.find(complement) != map.end()) { // Check if complement exists
                result.push_back(map[complement]); // Index of complement
                result.push_back(i); // Current index
                return result;
            }
            map[nums[i]] = i; // Store the current number and its index
        }
        return result; // Return empty if no solution found
    }
};


int main() {
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    vector<int> result = solution.twoSum(nums, target);

    for (int i = 0; i < nums.size(); i++) {
        cout << "nums[" << i << "] = " << nums[i] << ";" << endl;
    }
    
    if (!result.empty()) {
        cout << "Indices of the two numbers that add up to " << target << " are: ";
        cout << result[0] << " and " << result[1] << endl;
    } else {
        cout << "No solution found" << endl;
    }

    return 0;
}