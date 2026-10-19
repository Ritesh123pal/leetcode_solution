# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# LOGIC:
# 1. array ki length n me store kro
# 2. n size ka temp array bna lo
# 3. k ko n se mod kro taki agar k n se bda ho to uska effect na ho means extra rotation hata do.
# 4. loop se array ke har element pr jao.
# 5. temp array me (i+k)%n index pr nums[i] ko store kro.
# 6. temp array ko nums me copy kro taki nums me changes ho jaye.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """                                                    #PSEUDO CODE;
                                                          # 1.START
        n=len(nums)                                       # 2.set n=len(nums)
        temp=[0]*n                                        # 3.set temp array of size n
        k=k%n                                             # 4.set k=k%n (to handle cases where k>n)  
        for i in range(len(nums)):                        # 5.loop through the array
            temp[(i+k)%n]=nums[i]                         # 6.store nums[i] in temp[(i+k)%n]
        nums[:]=temp                                      # 7.copy temp array to nums
        return nums                                       # 8.return nums