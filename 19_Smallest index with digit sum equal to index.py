# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] <10:
              if nums[i]==i:
                return i
            sum=0
            while nums[i]!=0:  
                digit=nums[i]%10
                sum =sum +digit
                nums[i]=nums[i]//10
            if i == sum:
                return i
        return -1     
