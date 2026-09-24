# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        x=dividend
        y=divisor
        dividend=abs(dividend)
        divisor=abs(divisor)
        num=0
        while dividend>=divisor:
            value=divisor
            count=1
            while dividend>=value+value:
                value=value+value
                count=count+count
            dividend=dividend-value
            num=num+count   
        if (x<0 and y>0) or  (x>0 and y<0):
            return -num 
        if (num>pow(2,31)-1):
            return pow(2,31)-1      
        else:    
            return num