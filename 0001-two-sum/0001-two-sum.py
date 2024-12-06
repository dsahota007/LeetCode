class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)  #calc the length of the list and storing it in n 
        for i in range(n): #traverse the entire list of n 
            for j in range(i + 1, n): # inner loop - ensures that the same pair o fnum is not checked twice and avoid a num itself
                if nums[i] + nums[j]==target:
                    return[i,j]
        return None #if we cannot find pair than return None 
        