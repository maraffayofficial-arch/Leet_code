# LEETCODE PROBLEM 1 
#  NAME :   TWO SUM 

# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# SOLUTION



# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         k=0
#         l=0
#         for i in range(len(nums)):

#             for j in range(len(nums)):
            
#                 if nums[i]+nums[j]==target:
                
               
#                    if nums[i]!=nums[j] or i!=j: 
        
#                       k=i
#                       l=j
#                       break
      
#         return [k,l]
        

# CHECK WORKING 

# You may use these variabels interchangebly as they are from leetcode itself 

# nums = [2,7,11,15]
# nums = [2,4,11,3]
# nums=[3,3]
# target=6
# target = 9

# SS=Solution()
# SS.twoSum(nums,target)



        