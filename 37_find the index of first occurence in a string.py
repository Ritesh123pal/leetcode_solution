# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# LOGIC:
# 1.sabse pahle haystack aur neddle ki length calculate karenge.
# 2.range() me len(haystack)-len(neewdle)+1 likhenge taaki sirf valid starting indexes check hon.
# 3.ab for loop chalayenge,jo har index per jayegga .
# 4.har index i se needle ki length ke barabar character nikalenge.
# 5.nikalne ke liye haystack[i:i+len(needle)] ka use karenge.
# 6.ab nikla hua char needle ke baraber hai to return i kr denge .
# 7.aur agar nhi mila to return -1 kr denge . 
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """                                               #PSEUDO CODE:
                                                         # START:
        for i in range (len(haystack)-len(needle)+1):    #SET for i in range (len(haystack)-len(needle)+1).
            if haystack[i:i+len(needle)]==needle:        #.if haystack [i:i+len(needle)]== needle 
                return i                                 #. to return i,krenge
        return -1                                        # otherwise,return -1
                                                         # END