# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        show={}
        for i in range(len(nums)):
            if nums[i] in show and i-show[nums[i]]<=k:
               return True
            show[nums[i]]=i
        return False        