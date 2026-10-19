# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
# LOGIC:
# 1. pahle ek empty list bna lo jisme target indices store karenge.
# 2. nums ko sort kro taki target indices easily mil jaye.
# 3. loop se sorted array ke har element pr jao.
# 4. agar element target ke equal ho to uska index result list me store kro.
# 5. loop ke baad result list ko return kro.
class Solution(object):
    def targetIndices(self, nums, target):
        """                                    
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """                                     # PSEUDO CODE:
                                                 # 1.START
        result=[]                               # 2.set result as empty list
        ans = nums                              # 3.set ans as nums 
        ans.sort()                              # 4.sort ans in non-decreasing order        
        for i in range(len(ans)):               # 5.loop through the sorted array   
            if ans[i]==target:                  # 6.if ans[i] is equal to target
                result.append(i)                # 7.append the index i to result list
        return result                           # 8.return result list