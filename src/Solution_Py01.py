# The Brute Force method
# Starting Point (i): The outer loop picks where the subarray begins.
# Ending Point (j): The inner loop expands the subarray one element at a time to the right.
# Running Sum: As the subarray expands, the code adds the new element to current_sum.
# Update Record: If current_sum is greater than the best sum found so far (max_sum), it updates the record.

# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Start: max_sum is set to negative infinity.
# At i = 0 (Start with -2): Checks [-2], [-2, 1], [-2, 1, -3]... Best sum found for this start is -1.
# At i = 1 (Start with 1): Checks [1], [1, -3], [1, -3, 4]... Best sum found for this start is 2.
# At i = 3 (Start with 4):
# Subarray [4]: sum = 4
#Subarray [4, -1]: sum = 3
#Subarray [4, -1, 2]: sum = 5
#Subarray [4, -1, 2, 1]: sum = 6 (Update max_sum to 6).
#Subarray [4, -1, 2, 1, -5]: sum = 1
#At i = 8 (Start with 4): Checks [4]: sum = 4.
#Final Result: 6

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        
        return max_sum