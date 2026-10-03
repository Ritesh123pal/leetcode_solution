# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k.
#LOGIC: remove all occurrences of val in nums in-place
# 1.ek variable k=0 set karo.
# 2.ek loop chalao jisme i=0 se len(nums) tak jao.
# 3.agar nums[i] val ke barabar nahi hai to nums[k] ko nums[i] ke barabar set karo aur k ko 1 se increase karo.
# 4.ab jitni k ki value hai utni elements nums me honge jo val ke barabar nahi hai.
# 5.uske baad return k kar denge.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """                                       # PSEUDO CODE
                                                  # START
        k=0                                       #set k=0 
        for i in range(len(nums)):                #loop from i=0 to len(nums):
            if nums[i]!=val:                         #if nums[i] is not equal to val:
               nums[k]=nums[i]                            #set nums[k] to nums[i]
               k=k+1                                      #increment k
        return k                                  #return k
                                                  # END