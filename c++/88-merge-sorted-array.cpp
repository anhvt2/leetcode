#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Pointeer for the last element in the merged array
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1; // Last index of nums1

        // Merge nums1 and nums2 starting from the end
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                k--;
                i--;
            }
            else {
                nums1[k] = nums2[j];
                k--;
                j--;
            }
        }

        // If any elements left in nums2, copy over to nums1
        while (j >= 0) {
            nums1[k] = nums2[j];
            k--;
            j--;
        }

    }
};


int main() {
    // Example test case
    vector<int> nums1 = {1, 2, 3, 0, 0, 0};  // nums1 has extra space for nums2
    int m = 3;  // Number of initialized elements in nums1
    vector<int> nums2 = {2, 5, 6};  // nums2 contains elements to merge into nums1
    int n = 3;  // Number of elements in nums2

    Solution sol;
    sol.merge(nums1, m, nums2, n);

    // Print the result
    cout << "Merged Array: ";
    for (int num : nums1) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
