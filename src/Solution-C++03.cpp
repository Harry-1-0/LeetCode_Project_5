// Kadane's Algorithm Solution

// 1. Initialize two variables, maxSub and curSum, to the first element of the array and 0 respectively
// 2. Iterate through the array, adding each element to curSum
// 3. Update maxSub if curSum is greater than maxSub
// 4. If curSum drops below 0, reset it to 0
// 5. Return maxSub as the result

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0], curSum = 0;
        for (int num : nums) {
            if (curSum < 0) {
                curSum = 0;
            }
            curSum += num;
            maxSub = max(maxSub, curSum);
        }
        return maxSub;
    }
};
