# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=x
        sum=0
        if x<0:
            return False
        while(x>0):
            remainder=x%10
            sum=sum*10+remainder
            x=x/10
        return num==sum
                      
            
          