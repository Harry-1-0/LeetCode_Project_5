// Brute Force Solution

// 1. Try every possible subarray
// 2. Calculate its sum
// 3. Keep track of the maximum sum we see

// Time Complexity: O(n^2)
// Space Complexity: O(1)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size(), res = nums[0];
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i; j < n; j++) {
                cur += nums[j];
                res = max(res, cur);
            }
        }
        return res;
    }
};
