#  Dynamic Programming Solution:
# The Choice: At each index i, we decide: Should we start a new subarray at nums[i], or extend the best subarray from the previous index dp[i-1]?
# The dp Array: dp[i] stores the maximum sum of a subarray that ends exactly at index i.
# The Formula: dp[i] = max(nums[i], nums[i] + dp[i-1]). If the previous sum is negative, it's better to just start fresh with the current number.
# The Result: The largest value inside the dp array is the maximum subarray sum for the entire input.

# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Initial: dp = [-2, 1, -3, 4, -1, 2, 1, -5, 4] (Copy of nums)
# At i = 1 (num=1): max(1, 1 + (-2)). Result: 1. dp[1] = 1.
# At i = 2 (num=-3): max(-3, -3 + 1). Result: -2. dp[2] = -2.
# At i = 3 (num=4): max(4, 4 + (-2)). Result: 4. dp[3] = 4. (Start fresh!)
# At i = 4 (num=-1): max(-1, -1 + 4). Result: 3. dp[4] = 3.
# At i = 5 (num=2): max(2, 2 + 3). Result: 5. dp[5] = 5.
# At i = 6 (num=1): max(1, 1 + 5). Result: 6. dp[6] = 6.
# At i = 7 (num=-5): max(-5, -5 + 6). Result: 1. dp[7] = 1.
# At i = 8 (num=4): max(4, 4 + 1). Result: 5. dp[8] = 5.
# Final Result: max(dp) -> max([-2, 1, -2, 4, 3, 5, 6, 1, 5]) = 6.
# Final Result: max([-2, 1, -2, 4]) is 4.

class Solution:
    def maxSubArray(self, nums):
        dp = nums[:]  # copy array
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)