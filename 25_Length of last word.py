# Given a string s consisting of words and spaces, return the length of the last word in the string.
# LOGIC: length of last word
# 1.string ke last character se start karo.
# 2.ek variable count=0 set karo.
# 3.agar current character space nahi hai to count ko 1 se increase karo.
# 4.agar current character space hai aur count>0 hai to count return karo.
# 5.agar loop khatam ho jaye to count return karo.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int                              
        """                                     #   PSEUDO CODE  #
                                                # START 
        count=0                                 #set count=0
        for i in range(len(s)-1,-1,-1):         #start from last character of string and loop till first character of string:
            if  s[i]!=" ":                        #if current character is not space:
               count=count+1                         #increase count by 1
            elif count > 0:                       #elif count > 0:
                return count                          #return count   
        return count                            #return count
                                                #END