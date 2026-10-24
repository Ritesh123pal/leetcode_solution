# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
#LOGIC:
# pahle ek count variable lenge jisme no. of unique elements rahenge.
# aur ek empty list bhi lenge jisme unique element rahenge.
# ab loop chala ke condition dekr ans me unique elements dal denge aur sath me count ko bhi increase krte rahenge.
# ab ans me loop chala kr ans ke element ko nums me assign krenge with same index.
# ab count ko return kr denge .
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """                                          # PSEUDO CODE:
                                                # START        
        count=0                                 # set count=0     
        ans=[]                                  # Take an empty list ans
        for i in range(len(nums)):              # Traverse each element of nums
            if nums[i] not in  ans:             # if element is not in ans 
                ans.append(nums[i])             #    add the element to ans
                count+=1                        #    increase count by 1 
        for i in range (len(ans)):              # Traverse each element of ans 
            nums[i]=ans[i]                      # set nums[i]=ans[i]
        return count                            # return count
                                                # stop.  