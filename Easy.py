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



# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: Optional[ListNode]
#         :type l2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         dummy=ListNode(0)
#         curr=dummy
#         carry=0
    

#         while l1 or l2 or carry:
#             # extracting current values 
#             v1=l1.val if l1 else 0
#             v2=l2.val if l2 else 0
#             # now adding the values and calculating the carry value if it exist 
#             total=v1+v2+carry
#             carry=total//10
#             # make a new node 
#             curr.next=ListNode(total%10)
#             curr=curr.next

#             if l1:
#                 l1=l1.next
#             if l2:
#                 l2=l2.next
            
#         return dummy.next


# LEETCODE PROBLEM 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# solution 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
            