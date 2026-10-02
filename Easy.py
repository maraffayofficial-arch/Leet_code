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




# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p1=0
        p2=0
        sorted_array=[]
        while p1<len(nums1) and p2<len(nums2):
        # for p1 in range(len(nums1)):
            if nums1[p1]<=nums2[p2]:
                sorted_array.append(nums1[p1])
               
                p1+=1
            else:
                sorted_array.append(nums2[p2])
                
                p2+=1
        sorted_array.extend(nums1[p1:])
        sorted_array.extend(nums2[p2:])
        
        median_index=len(sorted_array)/2
        # print("median_index",median_index)

        if len(sorted_array)%2==0:
            median_index=median_index-1
            if sorted_array[int(median_index)]+ sorted_array[int(median_index)+1]==0:

                median_value=0
            else:
                median_value=((sorted_array[int(median_index)]+sorted_array[int(median_index)+1])/2)
            # print("if")
        else:
            median_index=int(median_index)
            median_value=sorted_array[median_index]
            # print("else")
            # print("median_index in else",median_index)
            
        
        return median_value
        # print(sorted_array)
        # print(median_value)
                
# Test 

# nums1 = [1,3]
# nums2 = [2]

# nums1 = [1,2]
# nums2 = [3,4]
# nums1 = [0,0]
# nums2 = [0,0]

nums1 = [2,2,4,4]
nums2 = [2,2,4,4]

obj=Solution()
obj.findMedianSortedArrays(nums1,nums2)







# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s. 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.


class Solution:
    def longestPalindrome(self, s: str) -> str:

       if len(s)==0:
            return ""
       start=0 #palindrome substring ka starting element
       len_best_pal=1 #longest palindrome ki len

       def longestpalindrome(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]: # asl main left right say left jayega and right jo hai wo left say right jayega increase hotay huay 
                # ye tb tk hoga jb tk s[right]==s[left] jesay he ye condition fail hui mtlb k yahan tk he substring paidrome thi or loop break hojayga or
                # return krdega left+1 kyu k left or right 1 dusray ko cross kr chukay hongay to left 1 extra step aagay hoga to left+1 hamari palindrome ka first element ya start index hoga jo k hman return krna hia 
                # or isi trhan kun k dono cross hogaye hain to right-left-1 say hmain puray palindrome substring ki length pta chl jayge
                left-=1
                right+=1
                
            return left+1,right-left-1

# is loop main hum sb substrngs ko compare krengay k sab say lambi konsi hai or start or len_best_pal ko update krtay jaingay
       for i in range(len(s)):
            
            s1,len1=longestpalindrome(i,i)
            if len1>len_best_pal:
                start,len_best_pal=s1,len1

            s2,len2=longestpalindrome(i,i+1)
            if len2>len_best_pal:
                start,len_best_pal=s2,len2

       return s[start:start+len_best_pal] # slicing start sa shuru and start+len and last element include nhi hoga slicing asay he kam krti hai
           
             
# Test check 
S=Solution()
s = "babad"

S.longestPalindrome(s)




# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows>=len(s) or numRows==1:
            return s
        rows=[""]*numRows
        current_row=0
        down=False
   
        for char in s:
            rows[current_row]+=char
            if current_row==0 or current_row==numRows-1:
                down = not down
            current_row+=1 if down else -1
        return "".join(rows)
            

# TEST CHECK 

S=Solution()
S.convert("raffay",3)



# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# this is the simple reversing integer  function

# def reverse(x: int) -> int:
#     result=0
#     while x!=0:
#         digit=x%10
#         result=result*10+digit
#         x=x//10
#     return result

# But the leetcode problem 7 will be done the below way 
class Solution:
    
    def reverse(self, x: int) -> int:
        int_min,int_max=-2**31,2**31-1
        sign=-1 if x<0 else 1
        x_abs=abs(x)
        res=0
        while x_abs!=0:
            digit=x_abs%10
            x_abs=x_abs//10
            if res>(int_max-digit)//10:
                 print("executed")
                 return 0
            res=res*10+digit
        return sign*res
        

x=123213

ss=Solution()
ss.reverse(x)



# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

# Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.
# The algorithm for `myAtoi(string s)` is as follows:

# 1. Whitespace: Ignore any leading whitespace (`" "`).
# 2. Signedness: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
# 3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# 4. Rounding: If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-231` should be rounded to `-231`, and integers greater than `231 - 1` should be rounded to `231 - 1`.

# Return the integer as the final result.


class Solution:
    def myAtoi(self, s: str) -> int:
        int_min,int_max= -2**31,2**31-1
        n=len(s)
        i=0

        while i<n and s[i]==" ":
            i+=1

        if i==n:
            return 0

        sign=1
        if s[i]=="+" or s[i]=="-":
            if s[i]=="-":
              sign=-1
            i+=1
        
        num=0
        while i<n and s[i].isdigit():
            digit=int(s[i])
            num=num*10 + digit
            i+=1

            if sign*num>int_max:
                return int_max
            if sign*num<int_min:
                
               return int_min
            
        result=sign*num
        if result<int_min:
            return int_min
        if result>int_max:
            return int_max

        return result


               
        

# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self,x: int) -> bool:
        flag=True
        int=str(x)
        b=len(int)
        
        for i in range(len(int)):
            if int[i]!=int[b-1]:
                flag=False
                return flag
            b-=1
                
        return flag

ss=Solution()
ss.isPalindrome(121)




# 10. Regular Expression Matching

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], '.'}

            if j + 1 < len(p) and p[j + 1] == '*':
                # Choice 1: Ignore '*' and preceding char
                # Choice 2: Use '*' if first_match is True
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

        s=Solution()
s.isMatch("aaa","a*a")


# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j=len(height)-1
        max_water=0
        while i<j:
            width=j-i
            water=width*min(height[i],height[j])
            max_water=max(max_water,water)
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water

s=Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])