// Dynamic Programming Solution

// 1. Create a dp array where dp[i] represents the maximum subarray sum ending at index i
// 2. For each index i, dp[i] is the maximum of nums[i] and nums[i] + dp[i - 1]
// 3. The answer is the maximum value in the dp array

// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums);
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(nums[i], nums[i] + dp[i - 1]);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
