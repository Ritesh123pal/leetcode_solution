# Write a function to find the longest common prefix string amongst an array of strings.
# LOGIC:
# 1.pahle check krenge ki strs khali to nhi h.
# 2.agr khali hoga to return"" kr denge
# 3.Ab first string ko nikal ke ek variable me assign karenge jisse check krenge baki str ko.
# 4.ab baki str me loop lagayenge.
# 5.ab check karenge ki baki str pahle vale str se  start ho rhe h ki nhi
# 6. uske bad prefix ko return kr denge.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """                                       # PSEUDO CODE:
                                               # START:
        if not strs:                           # 1.if strs is empty:
            return ""                               # 2.return empty str    
        prefix=strs[0]                         # 3.set prefix=strs
        for i in strs[1:]:                     # 4.strs[1:] ki har str i ke liye 
            while not i.startswith(prefix):        # 5.jab tak i,prefix se start nahi hoti    
                prefix=prefix[:-1]                     # 6.to prefix ka last char remove kr do
        return prefix                          # 7. prefix ko return kr do
                                               # 8.END 