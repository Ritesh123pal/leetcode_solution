# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq=[]
        for x in arr:
            if x not in freq:
                freq.append(x)
        list=[]
        for i in freq:
            list.append(arr.count(i))
        return len(list)==len(set(list))                    