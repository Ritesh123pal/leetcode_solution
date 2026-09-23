# Return true if n is a happy number, and false if not.
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen =[]
        while n!=1:
            if n in seen :
                return False
            seen.append(n)
            sum=0
            while n>0:
                digit=n%10
                sum = sum + digit*digit
                n=n//10
            n = sum        
        return True

 