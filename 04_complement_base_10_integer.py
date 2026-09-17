# Given an integer n, return its complement.
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=n
        mask=0
        if(n==0):
          return 1
        while(m!=0):
            mask=(mask<<1)|1
            m=m>>1
        return (~n)&mask
