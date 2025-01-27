class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the difference and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference exists in the dictionary
            if diff in num_map:
                return [num_map[diff], i]
            
            # Store the current number and its index in the dictionary
            num_map[num] = i

# Example usage:
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()
    
    # Example input
    nums = [2, 7, 11, 15]
    target = 9
    
    # Call the twoSum method
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
