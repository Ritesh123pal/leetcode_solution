# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# LOGIC:
# 1. Ek empty list ans banaye.(jisme dono arrays ke elements ko store karenge)
# 2. Ek loop chalao jisme i=0 se len(nums1) tak jao aur ans me nums1 ke elements ko append karo.
# 3. Ek loop chalao jisme i=0 se len(nums2) tak jao aur ans me nums2 ke elements ko append karo.
# 4. ans ko sort kar do.
# 5. n=ans ki length set karo.
# 6. Agar n odd hai to ans[n//2] ko return karo.
# 7. Agar n even hai to (ans[n//2 - 1] + ans[n//2]) / 2.0 ko return karo.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """                                              # PSEUDO CODE               
                                                     # START
        ans=[]                                       # 1.set ans=[] (empty list)
        for i in range (len(nums1)):                 # 2.loop from i=0 to len(nums1):           
            ans.append(nums1[i])                     # 3.append nums1[i] to ans
        for i in range (len(nums2)):                 # 4.loop from i=0 to len(nums2): 
            ans.append(nums2[i])                     # 5.append nums2[i] to ans
        ans.sort()                                   # 6.sort ans
        n=len(ans)                                   # 7.set n=len(ans)
        if n%2!=0:                                   # 8.if n is odd:
           return (ans[n//2])                        # 9.return ans[n//2]        
        else:                                        # 10.if n is even:
            return (ans[(n//2)-1]+ans[n//2])/2.0     # 11.return (ans[(n//2)-1]+ans[n//2])/2.0