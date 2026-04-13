#  Kadane's Algorithm Solution
# The "Dead Weight" Rule: We check if curSum < 0. If our current total is negative, it will only decrease the sum of any future subarray. So, we reset curSum to 0 (starting fresh from the current number).
# Accumulation: We add the current number num to our curSum.
# The Record: We use maxSub to keep track of the highest curSum we have ever encountered during the loop.

# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Start: maxSub = -2, curSum = 0
# At -2: curSum is 0. New curSum = 0 + (-2) = -2. maxSub is still -2.
# At 1: curSum (-2) is < 0. Reset curSum to 0. New curSum = 0 + 1 = 1. maxSub = 1.
# At -3: curSum (1) is not < 0. New curSum = 1 + (-3) = -2. maxSub is still 1.
# At 4: curSum (-2) is < 0. Reset curSum to 0. New curSum = 0 + 4 = 4. maxSub = 4.
# At -1: curSum (4) is not < 0. New curSum = 4 + (-1) = 3. maxSub is still 4.
# At 2: curSum (3) is not < 0. New curSum = 3 + 2 = 5. maxSub = 5.
# At 1: curSum (5) is not < 0. New curSum = 5 + 1 = 6. maxSub = 6.
# At -5: curSum (6) is not < 0. New curSum = 6 + (-5) = 1. maxSub is still 6.
# At 4: curSum (1) is not < 0. New curSum = 1 + 4 = 5. maxSub is still 6.
# Final Result: 6

class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub