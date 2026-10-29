# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# LOGIC:
# ISME HUM BINARY SEARCH KA LOGIC LGAYENGE
# 1.array ke mid wale element ko check kro.
# 2.agar target mid hi ho to uska index return kr do.
# 3.agar target mid element se bada ho to right side search kro.
# 4.agar target mid element se chota ho to mid ke left side search kro.
# 5.agar target na mile to uski insert position return karo.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """                                      # PSEUDO CODE:
                                           # START
        right=len(nums)-1                  # 1.set right=last index    (0 base indexing)
        left=0                             # 2.set left=first index  
        while left<=right:                 # 3.repeat step 4 to 7 while left<=right:
            mid=(left+right)//2             # 4.mid =(left+right)//2
            if nums[mid]==target:            # 5.if nums[mid]==target:
                return mid                       # return mid 
            elif nums[mid]>target:           # 6.elif nums[mid]>target:
                right=mid-1                     # set right=mid-1
            else:                            # 7.else:     
                left=mid+1                      # set left=mid+1
        return left                        #.return left     
        