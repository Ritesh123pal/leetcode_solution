# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#LOGIC: merge nums1 and nums2 into a single array sorted in non-decreasing order
# ek variable ans set karo empty list ke barabar.
# 1.ek loop chalao jisme i=0 se m tak jao aur ans me nums1[i] ko append karo.
# 2.ek loop chalao jisme j=0 se n tak jao aur ans me nums2[j] ko append karo.
# 3.ans ko sort kar do.
# 4.ek loop chalao jisme i=0 se m+n tak jao aur nums1[i] ko ans[i] ke barabar set karo.
# 5.ab nums1 me merged sorted array aa gaya hai.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """                                   #  PSEUDO CODE #
                                              # START
        ans=[]                                # set ans=[] empty list
        for i in range(m):                    # loop from i=0 to m:  where m  and n is number of element in nums1 and nums2
            ans.append(nums1[i])              # append nums1[i] to ans
        for j in range(n):                    # loop from j=0 to n:
            ans.append(nums2[j])              # append nums2[j] to ans 
        ans.sort()                            # sort ans
        for i in range(m+n):                  # loop from i=0 to m+n: 
            nums1[i]=ans[i]                   # set nums1[i] to ans[i]
        return nums1                          # return nums1 which is merged sorted array. 
                                              #END 